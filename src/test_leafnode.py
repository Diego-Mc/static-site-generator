import unittest

from leafnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestLeafNode(unittest.TestCase):
    def test_leaf_with_all(self):
        node = LeafNode("p", "Hello world!", {"data-testid": "test"})

        self.assertEqual("<p data-testid=\"test\">Hello world!</p>", node.to_html())

    def test_leaf_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_tag_none(self):
        node = LeafNode(None, "Hello")

        self.assertEqual("Hello", node.to_html())

    def test_leaf_tag_none_with_props(self):
        node = LeafNode(None, "Hello", {"test": "123"})

        self.assertEqual("Hello", node.to_html())

    def test_leaf_value_empty_string(self):
        node = LeafNode("p", "")

        self.assertEqual("<p></p>", node.to_html())

    def test_leaf_node_empty_string_with_props(self):
        node = LeafNode("p", "", {"test": "123"})

        self.assertEqual("<p test=\"123\"></p>", node.to_html())

class TestTextToHTMLNode(unittest.TestCase):
    def test_plaintext(self):
        node = TextNode("hello", TextType.TEXT)
        leaf = text_node_to_html_node(node)

        self.assertEqual("hello", leaf.to_html())

    def test_bold(self):
        node = TextNode("hello", TextType.BOLD)
        leaf = text_node_to_html_node(node)

        self.assertEqual("<b>hello</b>", leaf.to_html())


    def test_italic(self):
        node = TextNode("hello", TextType.ITALIC)
        leaf = text_node_to_html_node(node)

        self.assertEqual("<i>hello</i>", leaf.to_html())


    def test_code(self):
        node = TextNode("hello", TextType.CODE)
        leaf = text_node_to_html_node(node)

        self.assertEqual("<code>hello</code>", leaf.to_html())


    def test_link_with_href(self):
        node = TextNode("hello", TextType.LINK, "google.com")
        leaf = text_node_to_html_node(node)

        self.assertEqual("<a href=\"google.com\">hello</a>", leaf.to_html())

    def test_link_without_href(self):
        node = TextNode("hello", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_with_src(self):
        node = TextNode("hello", TextType.IMAGE, "image.png")
        leaf = text_node_to_html_node(node)

        self.assertEqual("<img src=\"image.png\" alt=\"hello\"></img>", leaf.to_html())

    def test_image_without_src(self):
        node = TextNode("hello", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()