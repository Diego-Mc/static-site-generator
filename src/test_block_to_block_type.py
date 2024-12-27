import unittest
from textwrap import dedent

from blocktype import BlockType
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        input = "This is just a paragraph"

        self.assertEqual(block_to_block_type(input), BlockType.PARAGRAPH)

    def test_heading(self):
        input1 = "# This is an heading1"
        input2 = "# This is an heading2"
        input3 = "# This is an heading3"
        input4 = "# This is an heading4"
        input5 = "# This is an heading5"
        input6 = "# This is an heading6"
        input7 = "#This is NOT an heading1"

        self.assertEqual(block_to_block_type(input1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input6), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type(input7), BlockType.HEADING)
        self.assertEqual(block_to_block_type(input7), BlockType.PARAGRAPH)

    def test_paragraph(self):
        input1 = "```CODE IS HERE!!```"
        input2 = dedent("""
            ```
            print()
            ```
        """).strip("\n")

        self.assertEqual(block_to_block_type(input1), BlockType.CODE)
        self.assertEqual(block_to_block_type(input2), BlockType.CODE)

    def test_paragraph(self):
        input1 = ">This is a quote"
        input2 = "> This is also a quote"

        self.assertEqual(block_to_block_type(input1), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(input2), BlockType.QUOTE)

    def test_unordered_list(self):
        input1 = dedent("""
            - Item 1
            * Item 2
            - Item 3
        """).strip("\n")
        input2 = dedent("""
            - Item 1
            * Item 2
            -Item 3
        """).strip("\n")
        input3 = dedent("""
            - Item 1
            *Item 2
            - Item 3
        """).strip("\n")

        self.assertEqual(block_to_block_type(input1), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input2), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input3), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(input2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(input3), BlockType.PARAGRAPH)

    def test_paragraph(self):
        input1 = dedent("""
            1. Item 1
            2. Item 2
            3. Item 3
        """).strip("\n")

        input2 = dedent("""
            1. Item 1
            2.Item 2
            3. Item 3
        """).strip("\n")

        input3 = dedent("""
            1. Item 1
            1. Item 2
            3. Item 3
        """).strip("\n")

        input4 = dedent("""
            1. Item 1
            - Item 2
            3. Item 3
        """).strip("\n")

        self.assertEqual(block_to_block_type(input1), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input2), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input3), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input4), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(input4), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(input2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(input3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(input4), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(input4), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()