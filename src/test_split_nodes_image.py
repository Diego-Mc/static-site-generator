import unittest

from split_nodes_image import split_nodes_images
from textnode import TextNode, TextType

class TestSplitNodesimage(unittest.TestCase):
    def test_no_image(self):
        node = TextNode("Hello not need for splitting here", TextType.TEXT)
        new_nodes = split_nodes_images([node])

        self.assertEqual(node, new_nodes[0])

    def text_images_many(self):
        node1 = TextNode("Hello ![to boot dev](https://www.boot.dev) not need for splitting here", TextType.TEXT)
        node2 = TextNode("Another ![to boot dev](https://www.boot.dev) one", TextType.TEXT)
        node3 = TextNode("And ![to boot dev](https://www.boot.dev) another", TextType.TEXT)
        new_nodes = split_nodes_images([node1, node2, node3])

        image_node = TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev")
        part1_start = TextNode("Hello ", TextType.TEXT)
        part1_end = TextNode(" not need for splitting here", TextType.TEXT)
        part2_start = TextNode("Another ", TextType.TEXT)
        part2_end = TextNode(" one", TextType.TEXT)
        part3_start = TextNode("And ", TextType.TEXT)
        part3_end = TextNode(" another", TextType.TEXT)

        self.assertListEqual([part1_start, image_node, part1_end,part2_start,image_node,part2_end,part3_start,image_node,part3_end], new_nodes)


if __name__ == "__main__":
    unittest.main()