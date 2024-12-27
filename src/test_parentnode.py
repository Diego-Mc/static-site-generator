import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_children_none(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    def test_parent_tag_none(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])

    def test_parent_children_empty(self):
        parent = ParentNode("p", [])

        self.assertEqual("<p></p>", parent.to_html())

    def test_parent_children_empty_with_props(self):
        parent = ParentNode("p", [], {"data-test": "hey"})

        self.assertEqual("<p data-test=\"hey\"></p>", parent.to_html())

    def test_parent_single_leaf_child(self):
        leaf = LeafNode(None, "Hello")
        parent = ParentNode("p", [leaf])

        self.assertEqual("<p>Hello</p>", parent.to_html())

    def test_parent_multiple_leaf_child(self):
        leaf1 = LeafNode(None, "Hello")
        leaf2 = LeafNode("b", "Bold")
        leaf3 = LeafNode("img", "", {"src": "image.png"})
        parent = ParentNode("div", [leaf1, leaf2, leaf3], {"test": "123"})

        self.assertEqual("<div test=\"123\">Hello<b>Bold</b><img src=\"image.png\"></img></div>", parent.to_html())

    def test_parent_multiple_parent_child(self):
        leaf1 = LeafNode(None, "Hello")
        leaf2 = LeafNode("b", "Bold")
        leaf3 = LeafNode("img", "", {"src": "image.png"})
        parent1 = ParentNode("div", [leaf1, leaf2, leaf3], {"test": "123"})
        parent2 = ParentNode("div", [leaf1, leaf2, leaf3], {"test": "123"})
        parent3 = ParentNode("div", [leaf1, leaf2, leaf3], {"test": "123"})

        parent_as_text = "<div test=\"123\">Hello<b>Bold</b><img src=\"image.png\"></img></div>"

        parent = ParentNode("span", [parent1, parent2, parent3], {"test": "456"})

        self.assertEqual(f"<span test=\"456\">{parent_as_text}{parent_as_text}{parent_as_text}</span>", parent.to_html())


if __name__ == "__main__":
    unittest.main()