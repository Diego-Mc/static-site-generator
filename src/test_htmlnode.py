import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"title": "test", "alt": "hello"})
        self.assertEqual(" title=\"test\" alt=\"hello\"", node.props_to_html())

    def test_props_to_html_one_val(self):
        node = HTMLNode(props={"title":"test"})
        self.assertEqual(" title=\"test\"", node.props_to_html())

    def test_ptops_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_clean(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())


if __name__ == "__main__":
    unittest.main()