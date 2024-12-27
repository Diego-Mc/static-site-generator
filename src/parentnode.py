from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag == None:
            raise ValueError("ParentNode must have a tag")
        if children == None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_str = ""
        if len(self.children) > 0:
            children_str = "".join(map(lambda node: node.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"