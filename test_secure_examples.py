import sqlite3
import unittest

from src.secure_coding_snippet_pairs import (
    find_user_by_username,
    hash_password,
    is_valid_username,
    safe_html_text,
    user_owns_resource,
    verify_password,
)


class SecureCodingTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE users (id INTEGER, username TEXT)")
        self.db.execute("INSERT INTO users VALUES (1, 'alice')")

    def tearDown(self):
        self.db.close()

    def test_parameterized_user_lookup(self):
        self.assertEqual(find_user_by_username(self.db, "alice")[0], 1)
        self.assertIsNone(find_user_by_username(self.db, "missing"))

    def test_html_encoding(self):
        self.assertEqual(safe_html_text("<tag>"), "&lt;tag&gt;")

    def test_password_hash_and_verify(self):
        salt, digest = hash_password("sample-password")
        self.assertTrue(verify_password("sample-password", salt, digest))
        self.assertFalse(verify_password("wrong-password", salt, digest))

    def test_authorization_ownership(self):
        self.assertTrue(user_owns_resource(7, 7))
        self.assertFalse(user_owns_resource(7, 8))

    def test_username_validation(self):
        self.assertTrue(is_valid_username("student_01"))
        self.assertFalse(is_valid_username("bad name"))

if __name__ == "__main__":
    unittest.main()
