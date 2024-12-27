import re;

def extract_markdown_images(text):
    return re.findall(r"!\[([\w\d\s]+)\]\(([\w:\/.@]+)\)", text)
