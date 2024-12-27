import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a url", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a url", TextType.LINK, "www.google.com")
        self.assertEqual(node, node2)

    def test_not_equal_type(self):
        node = TextNode("This is a test", TextType.LINK)
        node2 = TextNode("This is a test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("This is a test", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a test", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_equal_url_none(self):
        node = TextNode("This is a test", TextType.LINK, None)
        node2 = TextNode("This is a test", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is another test", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()