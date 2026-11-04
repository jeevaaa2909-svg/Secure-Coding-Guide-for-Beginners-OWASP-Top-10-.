"""Defensive secure-coding examples for beginner education.

The intentionally unsafe examples are described in comments only; no attack
payloads or automated exploitation are included.
"""
from __future__ import annotations

import hashlib
import hmac
import html
import os
import re
import sqlite3
from typing import Optional


# 1. SQL injection prevention: always bind user-supplied values as parameters.
def find_user_by_username(connection: sqlite3.Connection, username: str):
    return connection.execute(
        "SELECT id, username FROM users WHERE username = ?",
        (username,),
    ).fetchone()


# 2. Output encoding: encode untrusted text before placing it in HTML text.
def safe_html_text(value: str) -> str:
    return html.escape(value, quote=True)


# 3. Password storage: use a password-hashing KDF with a unique random salt.
# The iteration count should be reviewed against current platform guidance.
PBKDF2_ITERATIONS = 600_000


def hash_password(password: str, salt: Optional[bytes] = None) -> tuple[bytes, bytes]:
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string")
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    )
    return salt, digest


def verify_password(password: str, salt: bytes, expected_digest: bytes) -> bool:
    _, actual = hash_password(password, salt)
    return hmac.compare_digest(actual, expected_digest)


# 4. Authorization: check resource ownership on the server for every request.
def user_owns_resource(current_user_id: int, resource_owner_id: int) -> bool:
    return current_user_id == resource_owner_id


# 5. Input validation: validate expected formats at the application boundary.
_USERNAME_RE = re.compile(r"^[A-Za-z0-9_]{3,30}$")


def is_valid_username(username: str) -> bool:
    return bool(_USERNAME_RE.fullmatch(username))


def demo() -> None:
    print("Secure coding examples loaded.")
    salt, digest = hash_password("example-password")
    print("Password verification:", verify_password("example-password", salt, digest))
    print("HTML-escaped text:", safe_html_text("<hello>"))
    print("Username valid:", is_valid_username("student_01"))


if __name__ == "__main__":
    demo()
