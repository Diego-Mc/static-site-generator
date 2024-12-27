import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_multistep(self):
        input = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'

        result = text_to_textnodes(input)

        self.assertEqual([
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result
        )

    def test_only_text(self):
        input = "Hello world"

        self.assertEqual([TextNode("Hello world", TextType.TEXT)], text_to_textnodes(input))

    def test_heading(self):
        input = "# Hello"

        self.assertEqual([TextNode("# Hello", TextType.TEXT)], text_to_textnodes(input))

    def test_text(self):
        input = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"

        self.assertEqual([TextNode("I like Tolkien", TextType.BOLD), TextNode(". Read my ", TextType.TEXT), TextNode("first post here", TextType.LINK, "/majesty"), TextNode(" (sorry the link doesn't work yet)", TextType.TEXT)], text_to_textnodes(input))