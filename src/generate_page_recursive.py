import os

from generate_page import generate_page

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        new_path = f"{dir_path_content}/{file}"
        new_dest_path = f"{dest_dir_path}/{file}"
        if os.path.isfile(new_path):
            to_html_format = f"{new_dest_path[:-3]}.html"
            generate_page(new_path, template_path, to_html_format)
        else:
            if not os.path.exists(new_dest_path):
                os.makedirs(new_dest_path)
            generate_page_recursive(new_path, template_path, new_dest_path)
