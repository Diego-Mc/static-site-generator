from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value == None:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("LeafNode of type LINK must have a url")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("LeafNode of type IMAGE must have an url")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})