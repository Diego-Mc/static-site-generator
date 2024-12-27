
import unittest

from extract_title import extract_title

class TestParentNode(unittest.TestCase):
    def test_simple_title(self):
        input = "# Hello"

        self.assertEqual(extract_title(input), "Hello")

    def test_simple_title_trim(self):
        input = "#   Hello   "

        self.assertEqual(extract_title(input), "Hello")

    def test_not_a_title(self):
        input1 = "#Hello"
        input2 = "## Hello"
        input3 = "Hello"

        with self.assertRaises(Exception):
            extract_title(input1)

        with self.assertRaises(Exception):
            extract_title(input2)

        with self.assertRaises(Exception):
            extract_title(input3)

    def test_tew_headers(self):
        input = "# Hello\n\n# Hey"

        self.assertEqual(extract_title(input), "Hello")

if __name__ == "__main__":
    unittest.main()