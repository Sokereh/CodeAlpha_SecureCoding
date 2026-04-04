# CodeAlpha_SecureCoding_Review

## 📌 Project Overview
This project involves a **Secure Coding Review** of a Python-based authentication system. The goal was to identify critical vulnerabilities and provide remediation steps to secure the application.

## 🔍 Vulnerability Findings
1. **SQL Injection**: The original code used f-strings to build queries, allowing attackers to bypass authentication using strings like `' OR '1'='1`.
2. **Hardcoded Secrets**: Sensitive tokens were stored directly in the source code, making them visible to anyone with access to the repository.
3. **Insecure Credential Handling**: Lack of input sanitization allowed for potential database manipulation.

## ✅ Remediation Steps
* **Parameterized Queries**: Switched to using `?` placeholders to ensure user input is treated as data, not executable code.
* **Environment Variables**: Moved sensitive tokens to a `.env` file to keep secrets out of the version control system.
* **Input Validation**: Added logic to ensure only expected data formats are processed.

**Intern:** Okereh Star  
**Student ID:** CA/DF1/40819