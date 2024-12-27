import unittest
from textwrap import dedent

from htmlnode import HTMLNode
from blocktype import BlockType
from markdown_to_html_node import markdown_to_html_node

def global_parent(children):
    return HTMLNode("div", None, children)

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_header(self):
        input1 = '# This is a header'
        input2 = '## This is a header'
        input3 = '### This is a header'
        input4 = '#### This is a header'
        input5 = '##### This is a header'
        input6 = '###### This is a header'

        self.assertEqual(markdown_to_html_node(input1), global_parent([HTMLNode("h1", "This is a header")]))
        self.assertEqual(markdown_to_html_node(input2), global_parent([HTMLNode("h2", "This is a header")]))
        self.assertEqual(markdown_to_html_node(input3), global_parent([HTMLNode("h3", "This is a header")]))
        self.assertEqual(markdown_to_html_node(input4), global_parent([HTMLNode("h4", "This is a header")]))
        self.assertEqual(markdown_to_html_node(input5), global_parent([HTMLNode("h5", "This is a header")]))
        self.assertEqual(markdown_to_html_node(input6), global_parent([HTMLNode("h6", "This is a header")]))

    def test_paragraph(self):
        input = 'This is a paragraph'
        self.assertEqual(markdown_to_html_node(input), global_parent([HTMLNode("p", "This is a paragraph")]))

    def test_unordered_list(self):
        input1 = '- This is an unordered list'
        input2 = '* This is an unordered list'
        input3 = "-This is not an unordered list"
        input4 = "*This is not an unordered list"

        self.assertEqual(markdown_to_html_node(input1), global_parent([HTMLNode("ul", None, [HTMLNode("li", "This is an unordered list")])]))
        self.assertEqual(markdown_to_html_node(input2), global_parent([HTMLNode("ul", None, [HTMLNode("li", "This is an unordered list")])]))
        self.assertEqual(markdown_to_html_node(input3), global_parent([HTMLNode("p", "-This is not an unordered list")]))
        self.assertEqual(markdown_to_html_node(input4), global_parent([HTMLNode("p", "*This is not an unordered list")]))

    def test_ordered_list(self):
        input1 = '1. This is an ordered list'
        input2 = '1.This is not an ordered list'
        input3 = '2. This is not an ordered list'
        input4 = dedent("""
            1. This is an ordered list
            2. This is an ordered list
            3. This is an ordered list
        """).strip('\n')
        input5 = dedent("""
            1. This is an ordered list
            2.This is not an ordered list
            3. This is an ordered list
        """).strip('\n')

        self.assertEqual(markdown_to_html_node(input1), global_parent([HTMLNode("ol", None, [HTMLNode("li", "This is an ordered list")])]))
        self.assertEqual(markdown_to_html_node(input2), global_parent([HTMLNode("p", "1.This is not an ordered list")]))
        self.assertEqual(markdown_to_html_node(input3), global_parent([HTMLNode("p", "2. This is not an ordered list")]))
        self.assertEqual(markdown_to_html_node(input4), global_parent([HTMLNode("ol", None, [HTMLNode("li", "This is an ordered list"), HTMLNode("li", "This is an ordered list"), HTMLNode("li", "This is an ordered list")])]))
        self.assertEqual(markdown_to_html_node(input5), global_parent([HTMLNode("p", input5)]))

    def test_code_block(self):
        input1 = dedent("""
            ```python
            print("Hello world!")
            ```
        """).strip('\n')
        input2 = "`print(\"Hello world!\")`"
        self.assertEqual(markdown_to_html_node(input1), global_parent([HTMLNode("pre", None, [HTMLNode("code", "python\nprint(\"Hello world!\")\n")])]))
        self.assertEqual(markdown_to_html_node(input2), global_parent([HTMLNode("p", input2)]))

    def test_quote(self):
        input1 = '> This is a quote'
        input3 = '>This is also a quote'
        self.assertEqual(markdown_to_html_node(input1), global_parent([HTMLNode("blockquote", "This is a quote")]))
        self.assertEqual(markdown_to_html_node(input3), global_parent([HTMLNode("blockquote", "This is also a quote")]))

    def test_mixed(self):
        input = dedent("""
            # This is a header

            This is a paragraph

            - This is an unordered list

            1. This is an ordered list

            > This is a quote

            ```python
            print("Hello world!")
            ```

            * This is an unordered list

            2.This is not an ordered list

            -This is not an unordered list

            `This is not a code block`

            ####### This is not a header

            #This is not a header
        """).strip('\n')

        self.assertEqual(markdown_to_html_node(input), global_parent([
            HTMLNode("h1", "This is a header"),
            HTMLNode("p", "This is a paragraph"),
            HTMLNode("ul", None, [HTMLNode("li", "This is an unordered list")]),
            HTMLNode("ol", None, [HTMLNode("li", "This is an ordered list")]),
            HTMLNode("blockquote", "This is a quote"),
            HTMLNode("pre", None, [HTMLNode("code", "python\nprint(\"Hello world!\")\n")]),
            HTMLNode("ul", None, [HTMLNode("li", "This is an unordered list")]),
            HTMLNode("p", "2.This is not an ordered list"),
            HTMLNode("p", "-This is not an unordered list"),
            HTMLNode("p", "`This is not a code block`"),
            HTMLNode("p", "####### This is not a header"),
            HTMLNode("p", "#This is not a header")
        ]))