# Task 3: Secure Coding Review (SQL Injection)

## 📋 Project Summary
This project demonstrates the identification and remediation of a **SQL Injection (SQLi)** vulnerability in a Python/SQLite authentication module.

## 🛡️ Audit Findings
* **Vulnerability**: SQL Injection via string concatenation.
* **Exploit Used**: `' OR 1=1 --` (Bypasses authentication by commenting out the password check).
* **Impact**: Unauthorized access to the application without a valid password.

## ✅ Remediation
* **Parameterized Queries**: Replaced f-strings with `?` placeholders to separate SQL logic from user data.
* **Secure Data Handling**: Ensured that all user-supplied input is treated as literal text by the database driver.

**Intern:** Okereh Star  
**Student ID:** CA/DF1/40819  
**Academic Background:** MSc Cybersecurity and Digital Forensics
