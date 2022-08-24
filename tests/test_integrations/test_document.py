# Copyright (c) 2022 Johnathan P. Irvin
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
import pytest


def test_document_found(client) -> None:
    """
    Test that the main document can be found.
    
    Args:
        client (test_client): The test client for the Flask application.
    """    
    assert client.get(
        "/",
        follow_redirects=True,    
    ).status_code == 200

def test_document_not_found(client) -> None:
    """
    Test that the main document can be found.
    
    Args:
        client (test_client): The test client for the Flask application.
    """    
    assert client.get(
        "/notfound",
        follow_redirects=True,
    ).status_code == 404

@pytest.mark.parametrize("name, content", [
    ("viewport", "width=device-width, initial-scale=1"),
    ("description", "Johnathan Irvin is a software engineer and researcher based on planet Earth, serving the local solar system. You know, because remote work is a thing, and so is latency."),
    ("keywords", "Vue,JavaScript,HTML,CSS,Python,VueJS,Bootstrap,C#,Engineer,Software,Coding,Development"),
    ("author", "Johnathan Irvin"),
])
def test_document_meta_element(name: str, content: str, client) -> None:
    """
    Test that the document has the correct meta elements.

    Args:
        name (str): The name of the meta element.
        content (str): The content of the meta element.
        client (test_client): The test client for the Flask application.
    """
    assert client.get(
        '/',
        follow_redirects=True,
    ).data.decode().find(
        f"<meta name=\"{name}\" content=\"{content}\">"
    ) > 0
