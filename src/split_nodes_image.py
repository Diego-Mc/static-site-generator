from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images

def split_nodes_images(old_nodes):
    res = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode) or old_node.text_type != TextType.TEXT:
            res.append(old_node)
            continue
        markdown_image_infos = extract_markdown_images(old_node.text)
        if (len(markdown_image_infos) == 0):
            res.append(old_node)
            continue
        for info in markdown_image_infos:
            splitted = old_node.text.split(f"![{info[0]}]({info[1]})", 1)
            res.append(TextNode(splitted[0], TextType.TEXT))
            res.append(TextNode(info[0], TextType.IMAGE, info[1]))
            if splitted[1]:
                res.append(TextNode(splitted[1], TextType.TEXT))
    return res