from blocktype import BlockType


def block_to_block_type(block: str):
    if block.startswith(("# ","## ","### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    if all(line.startswith(("* ", "- ")) for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_ordered_list(text):
    lines = text.split("\n")
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return False
    return True
