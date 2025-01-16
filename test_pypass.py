#!/usr/bin/env python3

import pypass
import unittest

class TestPypassMethods(unittest.TestCase):

    def test_populate_word_dict_using_default_word_list(self):
        word_dict = pypass.populate_word_dict("word_lists/eff_large_wordlist.txt")
        self.assertEqual(len(word_dict), 7776, msg="Assert that the default word list has an appropriate length.")

    def test_populate_word_dict_using_non_existent_file(self):
        with self.assertRaises(FileNotFoundError, msg="Assert that a FileNotFoundError is raised when called with a non-existent file."):
            pypass.populate_word_dict("non_existent_file.txt")

    def test_populate_word_dict_using_file_with_non_appropriate_length(self):
        with self.assertRaises(RuntimeError, msg="Assert that a RuntimeError is raised when called with a file that does not have an appropriate length."):
            pypass.populate_word_dict("README.md")

    def test_validate_provided_file_using_valid_file(self):
        try:
            pypass.validate_provided_file("word_lists/eff_large_wordlist.txt")
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

    def test_generate_passwords(self):
        pass

    def test_generate_password(self):
        pass

    def test_generate_passphrase(self):
        pass

    def test_generate_index(self):
        pass

    def test_generate_pin(self):
        pass

    def test_print_passwords(self):
        pass

    def test_write_passwords(self):
        pass

if __name__ == "__main__":
    unittest.main()