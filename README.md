# Secure Coding Guide for Beginners (OWASP Top 10)

**Capstone Project 4 — Secure Software Development & Responsible AI**

A beginner-friendly, defensive learning project showing how to recognize common web-application security weaknesses and apply safer Python coding practices. The project is educational and deliberately contains no working exploit tools or attack automation.

## Project contents

- `docs/00_Capstone_4_Complete_Master_Portfolio.pdf` — original master project report.
- `docs/MASTER_PORTFOLIO.md` — Markdown version of the report for easy viewing on GitHub.
- `src/secure_coding_snippet_pairs.py` — five insecure-vs-secure examples, with runnable defensive examples.
- `automation/security_checklist_scanner.py` — lightweight Python AST scanner for selected unsafe coding patterns.
- `tests/test_secure_examples.py` — unit tests for the defensive examples.
- `.github/workflows/secure_coding_checklist.yml` — GitHub Actions workflow to run tests and the scanner.

## Requirements

- Python 3.10 or newer
- No third-party Python packages required

## Run locally

From the repository root:

```bash
python -m unittest discover -s tests -v
python src/secure_coding_snippet_pairs.py
python automation/security_checklist_scanner.py src/secure_coding_snippet_pairs.py
```

The scanner is a beginner teaching aid, not a complete security audit. A clean scan does not prove that an application is secure.

## GitHub upload

1. Download and extract this ZIP file.
2. Open GitHub and create a **New repository**.
3. Give it a name such as `secure-coding-guide-owasp`.
4. Upload the extracted **folder contents** (not the ZIP file itself) to the repository.
5. Commit the files.

## Ethical-use statement

Use these examples only to learn defensive programming and to review code you own or are authorized to assess. Do not test systems without explicit permission. Review AI-generated code manually and run appropriate tests before deployment.

## Topics

SQL parameterization, output encoding, password hashing, authorization checks, secure configuration, automated checks, and responsible AI use.
