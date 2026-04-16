Broken Access Control 
The flaw was that any user could access any profile by changing the userId in the URL. There was no authorization check. The fix verifies that the logged‑in user matches the requested profile.
OWASP reference: OWASP Top 10 2025 – Broken Access Control

Broken Access Control 
The original code let anyone access any account by entering a different user_id. The fix checks that the current user owns the account before returning data.
OWASP reference: OWASP Top 10 2025 – Broken Access Control

Cryptographic Failures 
The code used MD5, which is weak and easily cracked. The fix switches to SHA‑256, which is a modern and secure hashing algorithm.
OWASP reference: OWASP Top 10 2025 – Cryptographic Failures

Cryptographic Failures 
The code used SHA‑1, which is no longer secure. The fix uses PBKDF2 with SHA‑256, which is a recommended password hashing method.
OWASP reference: OWASP Top 10 2025 – Cryptographic Failures

Injection 
User input was placed directly into an SQL query, allowing attackers to inject malicious SQL. The fix uses a prepared statement, which separates code from data.
OWASP reference: OWASP Top 10 2025 – Injection

Injection 
The code trusted raw query parameters, which could allow NoSQL operators to be injected. The fix sanitizes the input by forcing it into a safe string.
OWASP reference: OWASP Top 10 2025 – Injection

Insecure Design
The password reset stored the new password in plain text. The fix hashes the password before saving it, which protects users even if the database is leaked.
OWASP reference: OWASP Top 10 2025 – Insecure Design

Software and Data Integrity Failures
The code loaded a script directly from a third‑party CDN. If the CDN is compromised, malicious code could run. The fix loads the script locally to reduce supply‑chain risk.
OWASP reference: OWASP Top 10 2025 – Software and Data Integrity Failures

Server‑Side Request Forgery 
The server made requests to any URL the user entered. Attackers could use this to reach internal systems. The fix restricts requests to a safe allow‑list.
OWASP reference: OWASP Top 10 2025 – Server‑Side Request Forgery

Identification and Authentication Failures
The code compared passwords directly, meaning passwords were stored in plain text. The fix uses a password hashing verification function instead.
OWASP reference: OWASP Top 10 2025 – Identification and Authentication Failures