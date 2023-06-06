#!/usr/bin/env python3
import os
import shutil
from typing import Callable


def copy_and_apply_func(src_dir: str, dst_dir: str, func: Callable[[str], None]) -> None:
    """
    Copy all the files, and directories from the source directory to the destination directory.

    Args:
        src_dir (str): The source directory.
        dst_dir (str): The destination directory.
        func (Callable[[str], None]): The function to apply to each file.
    """
    for root, _, files in os.walk(src_dir):
        for file in files:

            if file == "layout.html":
                continue

            src_path = os.path.join(root, file)

            dst_path = (
                os.path
                    .join(dst_dir, root, file)
                    .replace(src_dir, "")
                    .removeprefix(os.sep)
            )

            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
            func(dst_path)

def read_file(path: str) -> str:
    """
    Read the contents of a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    with open(path) as f:
        return f.read()

def copy_file(src: str, dest: str) -> None:
    """
    Copy a file from one location to another.

    Args:
        src (str): The path to the source file.
        dest (str): The path to the destination file.
    """
    with open(src, "rb") as f:
        content = f.read()

    with open(dest, "wb") as f:
        f.write(content)

def delete_directory(path: str) -> None:
    """
    Delete a directory.

    Args:
        path (str): The path to the directory.
    """
    if os.path.exists(path):
        shutil.rmtree(path)

def write_file(path: str, content: str) -> None:
    """
    Write the content to the file.

    Args:
        path (str): The path to the file.
        content (str): The content to write to the file.
    """
    with open(path, "w") as f:
        f.write(content)

def inject(template: str, content: str, tag="{% body %}") -> str:
    """
    Inject the content into the template. The content will be injected into
    the template at the location of the tag. The tag will be removed from
    the template.

    Args:
        template (str): The template to inject the content into.
        content (str): The content to inject into the template.
        tag (str, optional): The tag to inject the content into. Defaults to "{% body %}".

    Returns:
        str: The template with the content injected into it.
    """
    return template.replace(tag, content)

def minimize(html: str) -> str:
    """
    Minimize the HTML.

    Args:
        html (str): The HTML to minimize.

    Returns:
        str: The minimized HTML.
    """
    return " ".join(
        html
            .replace("\n", "")
            .replace("\t", "")
            .split()
    )

def main() -> None:
    """
    The main entry point for the script.
    """
    layout = read_file(os.path.join("src", "layout.html"))

    delete_directory("dist")
    copy_and_apply_func(
        src_dir="src",
        dst_dir="dist",
        func=lambda path: write_file(
            path=path,
            content=minimize(
                inject(
                    layout,
                    read_file(path),
                    tag="{% body %}"
                )
            ) if path.endswith(".html") else read_file(path)
        )
    )

    copy_file("CNAME", "dist/CNAME")
    copy_file("favicon.ico", "dist/favicon.ico")

if __name__ == "__main__":
    main()
