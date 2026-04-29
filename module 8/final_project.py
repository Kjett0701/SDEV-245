import argparse
import os
import re

PATTERNS = {
    "API Key": r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    "Password": r"password\s*[:=]\s*['\"].+['\"]",
    "Token": r"token\s*[:=]\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----"
}

def scan_file(path):
    results = []
    try:
        with open(path, "r", errors="ignore") as f:
            for line_num, line in enumerate(f, start=1):
                for name, pattern in PATTERNS.items():
                    if re.search(pattern, line):
                        results.append((path, line_num, name, line.strip()))
    except:
        pass
    return results

def scan_path(path):
    findings = []

    if os.path.isfile(path):
        findings.extend(scan_file(path))

    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                full = os.path.join(root, file)
                findings.extend(scan_file(full))

    return findings

def main():
    parser = argparse.ArgumentParser(description="Simple secret scanner.")
    parser.add_argument("path", nargs="?", help="File or directory to scan.")

    args = parser.parse_args()

    # If no path is given, scan THIS file
    if not args.path:
        args.path = __file__
        print(f"No path provided. Scanning this file instead: {args.path}")

    results = scan_path(args.path)

    if not results:
        print("No secrets found.")
        return

    print("\n=== Secret Scan Report ===")
    for file, line, kind, text in results:
        print(f"\nFile: {file}")
        print(f"Line: {line}")
        print(f"Type: {kind}")
        print(f"Match: {text}")

if __name__ == "__main__":
    main()

