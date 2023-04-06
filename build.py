#!/usr/bin/env python3
import os
import shutil


def get_output_directory(name: str) -> str:
    """
    Get the output directory for the build. If the directory does not exist,
    it will be created.

    Returns:
        str: The output directory.
    """
    if not os.path.exists(name):
        os.mkdir(name)
    
    return os.path.abspath(name)

def get_source_files() -> list[str]:
    """
    Get a list of all the source files in the src directory.

    Returns:
        list[str]: A list of paths to the source files.
    """
    return [
        os.path.join("src", item)
        for item in os.listdir("src")
    ]

def get_output_file(src_file: str, output_dir: str) -> str:
    """
    Get the output file for a source file. The output file will be in the
    provided output directory.

    Args:
        src_file (str): The path to the source file.
        output_dir (str): The path to the output directory.

    Returns:
        str: The path to the output file.
    """
    return os.path.join(
        get_output_directory(output_dir),
        os.path.basename(src_file)
    )

def get_pages() -> list[str]:
    """
    Get a list of all the pages in the src directory.

    Returns:
        list[str]: A list of paths to the pages.
    """
    return [
        os.path.join("src", item)
        for item in os.listdir("src")
        if item.endswith(".html") and item != "layout.html"
    ]

def get_layout() -> str:
    """
    Get the layout file.

    Returns:
        str: The path to the layout file.
    """
    return os.path.join("src", "layout.html")

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
    
def write_file(path: str, content: str) -> None:
    """
    Write the content to a file.

    Args:
        path (str): The path to the file.
        content (str): The content to write to the file.
    """
    with open(path, "w") as f:
        f.write(content)

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
    return html.replace("\n", "").replace("\t", "").replace("  ", "")


def main() -> None:
    """
    The main entry point for the script.
    """
    layout = read_file(
        get_layout()
    )

    delete_directory("dist")

    for page in get_pages():
        write_file(
            get_output_file(
                src_file=page,
                output_dir="dist"
            ),
            minimize(
                inject(
                    layout,
                    read_file(page),
                    tag="{% body %}"
                )
            )
        )

        copy_file("CNAME", "dist/CNAME")
        copy_file("favicon.ico", "dist/favicon.ico")

if __name__ == "__main__":
    main()
