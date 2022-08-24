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
import bs4
import pytest

ARTICLE_SLUGS: list = [
    "articles/2020/10/10/hello-world",
    "articles/2022/07/14/goodbye-cruel-world",
]

@pytest.mark.parametrize("article_slug", ARTICLE_SLUGS)
def test_article_found(article_slug: str, client) -> None:
    """
    Test that an article can be found.

    Args:
        article_slug (str): The slug of the article to find.
        client (website.app.test_client): The test client for the Flask application.
    """    
    assert client.get(
        f"/{article_slug}",
        follow_redirects=True,
    ).status_code == 200

@pytest.mark.parametrize("article_slug", ARTICLE_SLUGS)
def test_article_snapshots(article_slug: str, client, snapshot) -> None:
    """
    Test that an article can be found.

    Args:
        article_slug (str): The slug of the article to find.
        client (website.app.test_client): The test client for the Flask application.
        snapshot (pytest_snapshot.plugin.Snapshot): The snapshot plugin.
    """    
    snapshot.snapshot_dir = "tests/snapshots"
    html = client.get(
        f"/{article_slug}",
        follow_redirects=True,
    ).text
    soup = bs4.BeautifulSoup(html, "html.parser")

    snapshot.assert_match(
        soup.body.prettify(),
        article_slug.split("/")[-1] + ".snapshot.html"
    )
