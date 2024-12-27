import unittest;
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_two_links(self):
        input = 'This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)'
        extracted = extract_markdown_links(input)

        self.assertListEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], extracted)

    def test_no_links(self):
        input = 'This is text with no links'
        extracted = extract_markdown_links(input)

        self.assertListEqual([], extracted)


if __name__ == "__main__":
    unittest.main()