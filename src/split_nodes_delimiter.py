from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode) or old_node.text_type != TextType.TEXT or delimiter not in old_node.text or len(delimiter) == 0:
            res.append(old_node)
            continue
        splits = old_node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise Exception("Invalid markdown or delimiter")
        for i in range(0, len(splits)):
            if len(splits[i]) == 0:
                continue
            if i % 2 == 0:
                res.append(TextNode(splits[i], TextType.TEXT))
            else:
                res.append(TextNode(splits[i], text_type))
    return res