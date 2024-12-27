import os

from extract_title import extract_title

from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = None
    with open(from_path) as f:
        markdown = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    root_node = markdown_to_html_node(markdown)
    as_html = root_node.to_html()

    title = extract_title(markdown)

    updated_html = template.replace("{{ Title }}", title).replace("{{ Content }}", as_html)

    with open(dest_path, "w") as f:
        f.write(updated_html)