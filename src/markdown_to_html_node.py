from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from blocktype import BlockType
from parentnode import ParentNode
from leafnode import text_node_to_html_node
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

def get_heading_suffix(text):
    i = 1
    while text.startswith("#" * i):
        i += 1
    final = i - 1
    return ("#" * final, final)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        match(block_to_block_type(block)):
            case BlockType.HEADING:
                suffix, level = get_heading_suffix(block)
                text = block.replace(f"{suffix} ", "", 1)
                text_nodes = text_to_textnodes(text)
                as_html_nodes = list(map(text_node_to_html_node, text_nodes))
                children.append(ParentNode(f"h{level}", as_html_nodes))
            case BlockType.PARAGRAPH:
                text_nodes = text_to_textnodes(block)
                as_html_nodes = list(map(text_node_to_html_node, text_nodes))
                children.append(ParentNode("p", as_html_nodes))
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                without_suffix = list((map(lambda x: x[2:], lines)))
                lines_text_nodes = list(map(text_to_textnodes, without_suffix))
                ul_children_values = list(map(lambda line: list(map(lambda node: text_node_to_html_node(node), line)), lines_text_nodes))
                ul_children = list(map(lambda x: ParentNode("li", x), ul_children_values))
                children.append(ParentNode("ul", ul_children))
            case BlockType.ORDERED_LIST:
                # TODO: rename and reuse
                lines = block.split("\n")
                without_suffix = list((map(lambda x: x[3:], lines)))
                lines_text_nodes = list(map(text_to_textnodes, without_suffix))
                ul_children_values = list(map(lambda line: list(map(lambda node: text_node_to_html_node(node), line)), lines_text_nodes))
                ul_children = list(map(lambda x: ParentNode("li", x), ul_children_values))
                children.append(ParentNode("ol", ul_children))
            case BlockType.CODE:
                text_nodes = text_to_textnodes(block[3:-3])
                as_html_nodes = list(map(text_node_to_html_node, text_nodes))
                children.append(ParentNode("pre", [ParentNode("code", as_html_nodes)]))
            case BlockType.QUOTE:
                text_nodes = text_to_textnodes(block[1:].strip())
                as_html_nodes = list(map(text_node_to_html_node, text_nodes))
                children.append(ParentNode("blockquote", as_html_nodes))
    return ParentNode("div", children)