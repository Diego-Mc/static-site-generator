import os
import shutil

from generate_page_recursive import generate_page_recursive

print("Hello world")

does_public_exists = os.path.exists("public")

if does_public_exists:
    shutil.rmtree("public")
os.mkdir("public")

def copy_files(path):
    for file in os.listdir(path):
        print(file)
        new_path = f"{path}/{file}"
        extention = "/".join(new_path.split("/")[1:])
        new_public_path = f"public/{extention}"
        if os.path.isfile(new_path):
            shutil.copy(new_path, new_public_path)
        else:
            os.mkdir(new_public_path)
            copy_files(new_path)

copy_files("static")

generate_page_recursive("content", "template.html", "public")