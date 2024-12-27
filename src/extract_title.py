from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from markdown_to_html_node import get_heading_suffix
from blocktype import BlockType

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            (suffix, level) = get_heading_suffix(block)
            if level == 1:
                return block.replace(f"{suffix} ", "", 1).strip()
    raise Exception("No title found")
