import argparse
import os
import re
import logging

# Set up basic logging so we can track what's happening
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Regex patterns to look for common hardcoded secrets
PATTERNS = {
    "API Key": r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    "Password": r"password\s*[:=]\s*['\"].+['\"]",
    "Token": r"token\s*[:=]\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----"
}

def scan_file(path):
    results = []
    logging.info(f"Scanning file: {path}")

    try:
        # Open file safely and ignore encoding issues
        with open(path, "r", errors="ignore") as f:
            for line_num, line in enumerate(f, start=1):
                # Check each line against all patterns
                for name, pattern in PATTERNS.items():
                    if re.search(pattern, line):
                        logging.warning(f"Secret found in {path} on line {line_num}: {name}")
                        results.append((path, line_num, name, line.strip()))
    except Exception as e:
        # Log any file read errors
        logging.error(f"Error reading file {path}: {e}")

    return results

def scan_path(path):
    findings = []

    # If it's a single file, scan it
    if os.path.isfile(path):
        logging.info(f"Target is a file: {path}")
        findings.extend(scan_file(path))

    # If it's a directory, walk through all files
    elif os.path.isdir(path):
        logging.info(f"Target is a directory: {path}")
        for root, _, files in os.walk(path):
            for file in files:
                full = os.path.join(root, file)
                findings.extend(scan_file(full))

    else:
        # Invalid path provided
        logging.error(f"Invalid path: {path}")

    return findings

def main():
    # Set up CLI argument parsing
    parser = argparse.ArgumentParser(description="Simple secret scanner.")
    parser.add_argument("path", nargs="?", help="File or directory to scan.")

    args = parser.parse_args()

    # If no path is given, scan this script itself
    if not args.path:
        args.path = __file__
        logging.info(f"No path provided. Scanning this file instead: {args.path}")

    logging.info(f"Starting scan on: {args.path}")
    results = scan_path(args.path)

    # If nothing was found, let the user know
    if not results:
        logging.info("Scan complete. No secrets found.")
        print("No secrets found.")
        return

    # Print a simple report of all findings
    print("\n=== Secret Scan Report ===")
    for file, line, kind, text in results:
        print(f"\nFile: {file}")
        print(f"Line: {line}")
        print(f"Type: {kind}")
        print(f"Match: {text}")

    logging.info("Scan complete. Secrets were found and reported.")

if __name__ == "__main__":
    main()

