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

if __name__ == "__main__":
    unittest.main()