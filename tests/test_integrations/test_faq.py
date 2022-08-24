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


def test_faq(client):
    """
    Test the FAQ page.

    Args:
        client (test_client): The test client.
    """
    response = client.get(
        '/faq',
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert 'Frequently Asked Questions' in response.text

@pytest.mark.parametrize('question', [
    "What experience do you have in the field of software development?",
    "How did you get into software development?",
    "What are your strengths and weaknesses?",
    "What salary are you looking for?",
    "Are you willing to relocate?",
    "When can you start?",
    "Describe a time when you had to overcome a challenge at work.",
    "Describe a time when you made a mistake at work and how you handled it.",
])
def test_faq_questions(client, question: str):
    """
    Test the FAQ questions.

    Args:
        client (test_client): The test client.
        question (str): The question to test.
    """
    response = client.get(
        '/faq',
        follow_redirects=True,
    )

    assert question in response.text
