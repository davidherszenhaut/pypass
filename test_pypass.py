#!/usr/bin/env python3

from unittest.mock import patch
from io import StringIO

import os
import pypass
import unittest

DEFAULT_WORDLIST = "word_lists/eff_large_wordlist.txt"
PASSWORDS = ["password1", "password2", "password3"]
OUTPUT_FILE = "test_write_passwords.txt"

class TestPypassMethods(unittest.TestCase):

    def test_populate_word_dict_using_default_word_list(self):
        word_dict = pypass.populate_word_dict(DEFAULT_WORDLIST)
        self.assertEqual(len(word_dict), 7776, msg="Assert that the default word list has an appropriate length.")

    def test_populate_word_dict_using_non_existent_file(self):
        with self.assertRaises(FileNotFoundError, msg="Assert that a FileNotFoundError is raised when called with a non-existent file."):
            pypass.populate_word_dict("non_existent_file.txt")

    def test_populate_word_dict_using_file_with_non_appropriate_length(self):
        with self.assertRaises(RuntimeError, msg="Assert that a RuntimeError is raised when called with a file that does not have an appropriate length."):
            pypass.populate_word_dict("README.md")

    def test_validate_provided_file_using_valid_file(self):
        try:
            pypass.validate_provided_file(DEFAULT_WORDLIST)
        except Exception:
            self.fail("Valid word list file was unexpectedly not validated.")
    
    def test_validate_provided_file_using_non_existent_file(self):
        with self.assertRaises(FileNotFoundError, msg="Assert that a FileNotFoundError is raised when called with a non-existent file."):
            pypass.validate_provided_file("non_existent_file.txt")

    def test_validate_provided_file_using_file_with_non_appropriate_length(self):
        with self.assertRaises(RuntimeError, msg="Assert that a RuntimeError is raised when called with a file that does not have an appropriate length."):
            pypass.validate_provided_file("README.md")

    def test_get_password_length_default_passphrase(self):
        length = pypass.get_password_length("passphrase", None)
        self.assertEqual(length, 6)

    def test_get_password_length_user_defined_passphrase(self):
        length = pypass.get_password_length("passphrase", 11)
        self.assertEqual(length, 11)

    def test_get_password_length_default_password(self):
        length = pypass.get_password_length("password", None)
        self.assertEqual(length, 12)

    def test_get_password_length_user_defined_password(self):
        length = pypass.get_password_length("password", 22)
        self.assertEqual(length, 22)

    def test_get_password_length_default_pin(self):
        length = pypass.get_password_length("pin", None)
        self.assertEqual(length, 4)

    def test_get_password_length_user_defined_pin(self):
        length = pypass.get_password_length("pin", 33)
        self.assertEqual(length, 33)

    def test_generate_passwords_repeat_count(self):
        word_dict = None
        character = None
        kind = "password"
        length = pypass.get_password_length(kind, 17)
        repeat = 17
        separator = None
        passwords = pypass.generate_passwords(word_dict, character, kind, length, repeat, separator)
        self.assertEqual(repeat, len(passwords))

    def test_generate_password_default_length(self):
        word_dict = None
        character = None
        kind = "password"
        length = pypass.get_password_length(kind, None)
        separator = None
        password = pypass.generate_password(word_dict, character, kind, length, separator)
        self.assertEqual(len(password), length)
        self.assertTrue(password.isalnum())

    def test_generate_password_user_defined_length(self):
        word_dict = None
        character = None
        kind = "password"
        length = pypass.get_password_length(kind, 17)
        separator = None
        password = pypass.generate_password(word_dict, character, kind, length, separator)
        self.assertEqual(len(password), length)
        self.assertTrue(password.isalnum())

    def test_generate_passphrase_default_word_list_no_special_character_default_length_default_separator(self):
        word_dict = pypass.populate_word_dict(DEFAULT_WORDLIST)
        character = False
        kind = "passphrase"
        length = pypass.get_password_length(kind, None)
        separator = " "
        passphrase = pypass.generate_passphrase(word_dict, character, length, separator)
        self.assertEqual(length - 1, passphrase.count(separator))
        self.assertTrue(all(x.isalpha() or x.isspace() or x == "-" for x in passphrase))

    def test_generate_passphrase_default_word_list_with_special_character_default_length_default_separator(self):
        word_dict = pypass.populate_word_dict(DEFAULT_WORDLIST)
        character = True
        kind = "passphrase"
        length = pypass.get_password_length(kind, None)
        separator = " "
        passphrase = pypass.generate_passphrase(word_dict, character, length, separator)
        self.assertEqual(length - 1, passphrase.count(separator))
        self.assertFalse(all(x.isalpha() or x.isspace() for x in passphrase))

    def test_generate_passphrase_default_word_list_no_special_character_user_defined_length_default_separator(self):
        word_dict = pypass.populate_word_dict(DEFAULT_WORDLIST)
        character = False
        kind = "passphrase"
        length = pypass.get_password_length(kind, 17)
        separator = " "
        passphrase = pypass.generate_passphrase(word_dict, character, length, separator)
        self.assertEqual(length - 1, passphrase.count(separator))
        self.assertTrue(all(x.isalpha() or x.isspace() or x == "-" for x in passphrase))

    def test_generate_passphrase_default_word_list_no_special_character_default_length_user_defined_separator(self):
        word_dict = pypass.populate_word_dict(DEFAULT_WORDLIST)
        character = False
        kind = "passphrase"
        length = pypass.get_password_length(kind, None)
        separator = "!"
        passphrase = pypass.generate_passphrase(word_dict, character, length, separator)
        self.assertEqual(length - 1, passphrase.count(separator))
        self.assertFalse(all(x.isalpha() or x.isspace() for x in passphrase))

    def test_generate_index_returns_appropriate_length(self):
        index = pypass.generate_index()
        self.assertEqual(len(index), 5)

    def test_generate_index_returns_appropriate_characters(self):
        index = pypass.generate_index()
        self.assertTrue(index.isdigit())

    def test_generate_pin_returns_appropriate_length(self):
        pin = pypass.generate_pin(11)
        self.assertEqual(len(pin), 11)

    def test_generate_pin_uses_appropriate_characters(self):
        pin = pypass.generate_pin(11)
        self.assertTrue(pin.isdigit())

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_passwords_with_quiet_mode(self, mock_stdout):
        pypass.print_passwords(PASSWORDS, True)
        assert mock_stdout.getvalue() == "Quiet argument was chosen. Passwords will not be printed.\n"

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_passwords_without_quiet_mode(self, mock_stdout):
        pypass.print_passwords(PASSWORDS, False)
        assert mock_stdout.getvalue() == "\n".join(PASSWORDS) + "\n"

    def test_write_passwords_file_is_created(self):
        pypass.write_passwords(PASSWORDS, OUTPUT_FILE)
        self.assertEqual(os.path.isfile(OUTPUT_FILE), True)
        os.remove(OUTPUT_FILE)

    def test_write_passwords_file_has_all_passwords(self):
        pypass.write_passwords(PASSWORDS, OUTPUT_FILE)
        with open(OUTPUT_FILE, "r") as written_passwords:
            line_count = written_passwords.readlines()
            self.assertEqual(len(line_count), len(PASSWORDS))
        os.remove(OUTPUT_FILE)

if __name__ == "__main__":
    unittest.main()