import re;

def extract_markdown_links(text):
    return re.findall(r"\[([\w\d\s]+)\]\(([\w:\/.@]+)\)", text)
