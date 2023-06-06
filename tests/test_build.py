# Copyright (c) 2021-2023 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from unittest.mock import call, mock_open, patch

import pytest

from build import copy_file, delete_directory, minimize, read_file, write_file


def test_read_file():
    """
    Test the read_file function.
    """
    with patch("build.open", mock_open(read_data="data")) as mock_file:
        assert read_file("path") == "data"
        mock_file.assert_called_once_with("path")

def test_write_file():
    """
    Test the write_file function.
    """
    with patch("build.open", mock_open()) as mock_file:
        write_file("path", "data")

        mock_file.assert_called_once_with("path", "w")
        mock_file().write.assert_called_once_with("data")


def test_copy_file():
    """
    Test the copy_file function.
    """
    with patch("build.open", mock_open()) as mock_file:
        copy_file("src", "dst")

        mock_file.assert_has_calls(
            [
                call("src", "rb"),
                call("dst", "wb"),
            ],
            any_order=True
        )

@pytest.mark.parametrize(
    "path, exists",
    [
        ("path", True),
        ("path", False),
    ]
)
def test_delete_directory(path, exists):
    with patch("build.os.path.exists", return_value=exists) as mock_exists:
        with patch("build.shutil.rmtree") as mock_rmtree:
            delete_directory(path)

            mock_exists.assert_called_once_with("path")

            if exists:
                mock_rmtree.assert_called_once_with("path")
            else:
                mock_rmtree.assert_not_called()

@pytest.mark.parametrize(
    "unminimized, minimized",
    [
        ("data", "data"),
        ("data\n", "data"),
        ("data\t", "data"),
        ("data  ", "data"),
        ("data\n\t", "data"),
        ("data\n  ", "data"),
        ("data\t  ", "data"),
        ("data\n\t  ", "data"),
        ("data\n\t  data", "data data"),
    ]
)
def test_minimize(unminimized, minimized):
    assert minimize(unminimized) == minimized
