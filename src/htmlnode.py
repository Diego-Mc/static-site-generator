class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(map(lambda val: f" {val[0]}=\"{val[1]}\"" ,self.props.items()))

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props_to_html()})"

