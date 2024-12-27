import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_plaintext(self):
        node = TextNode("Hello not need for splitting here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)

        self.assertEqual(node, new_nodes[0])

    def text_split_plaintext_many(self):
        node1 = TextNode("Hello not need for splitting here", TextType.TEXT)
        node2 = TextNode("Another one", TextType.TEXT)
        node3 = TextNode("And another", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "", TextType.TEXT)

        self.assertEqual(node1, new_nodes[0])
        self.assertEqual(node2, new_nodes[1])
        self.assertEqual(node3, new_nodes[2])

    def test_split_bold(self):
        node = TextNode("Hello **this is bold** hey", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        part1 = TextNode("Hello ", TextType.TEXT)
        part2 = TextNode("this is bold", TextType.BOLD)
        part3 = TextNode(" hey", TextType.TEXT)

        self.assertEqual(part1, new_nodes[0])
        self.assertEqual(part2, new_nodes[1])
        self.assertEqual(part3, new_nodes[2])

    def test_split_bold_multiple_same_line(self):
        node = TextNode("Hello **this is bold** hey **and this as well**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        part1 = TextNode("Hello ", TextType.TEXT)
        part2 = TextNode("this is bold", TextType.BOLD)
        part3 = TextNode(" hey ", TextType.TEXT)
        part4 = TextNode("and this as well", TextType.BOLD)

        self.assertEqual(part1, new_nodes[0])
        self.assertEqual(part2, new_nodes[1])
        self.assertEqual(part3, new_nodes[2])
        self.assertEqual(part4, new_nodes[3])

    def test_split_code_multiple_same_line(self):
        node = TextNode("Hello `this is code` hey `and this as well`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        part1 = TextNode("Hello ", TextType.TEXT)
        part2 = TextNode("this is code", TextType.CODE)
        part3 = TextNode(" hey ", TextType.TEXT)
        part4 = TextNode("and this as well", TextType.CODE)

        self.assertEqual(part1, new_nodes[0])
        self.assertEqual(part2, new_nodes[1])
        self.assertEqual(part3, new_nodes[2])
        self.assertEqual(part4, new_nodes[3])


if __name__ == "__main__":
    unittest.main()