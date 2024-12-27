import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_one_block(self):
        markdown = """This is a single block of text"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(["This is a single block of text"], result)

    def test_multi_block(self):
        markdown = """This is a single block of text

        And here is **another** one

        And this ![my alt](image.png) image"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(["This is a single block of text", "And here is **another** one", "And this ![my alt](image.png) image"], result)

    def test_multi_block_with_trim(self):
        markdown = """This is a single block of text




        And here is **another** one



        And this ![my alt](image.png) image"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(["This is a single block of text", "And here is **another** one", "And this ![my alt](image.png) image"], result)




if __name__ == "__main__":
    unittest.main()