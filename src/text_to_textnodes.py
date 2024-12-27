from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_images
from split_nodes_link import split_nodes_link

delimiters = {
    TextType.BOLD: "**",
    TextType.CODE: "`",
    TextType.ITALIC: "*",
}

def text_to_textnodes(text):
    process = [TextNode(text, TextType.TEXT)]
    process = split_nodes_delimiter(process, delimiters[TextType.BOLD], TextType.BOLD)
    process = split_nodes_delimiter(process, delimiters[TextType.ITALIC], TextType.ITALIC)
    process = split_nodes_delimiter(process, delimiters[TextType.CODE], TextType.CODE)
    process = split_nodes_images(process)
    process = split_nodes_link(process)
    return process



