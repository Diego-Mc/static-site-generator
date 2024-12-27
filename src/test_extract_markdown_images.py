import unittest;
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_two_images(self):
        input = 'text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"'
        extracted = extract_markdown_images(input)

        self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], extracted)

    def test_no_images(self):
        input = 'text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"'
        extracted = extract_markdown_images(input)

        self.assertListEqual([], extracted)


if __name__ == "__main__":
    unittest.main()