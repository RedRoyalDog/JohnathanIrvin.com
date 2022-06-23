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
import flask
import markdown

from website.repositories import Repository, blog_repositories

app = flask.Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
repo = blog_repositories.PostRepository('blog')

@app.route('/')
def index() -> str:
    return flask.render_template(
        'index.pug',
        posts=sorted(
            repo.get_all(),
            key=lambda post: post.date,
            reverse=True,
        )
    )

@app.route('/articles/<int:year>/<int:month>/<int:day>/<string:description>')
def article(year: int, month: int, day: int, description: str) -> str:
    try:
        post = repo.get(f"{year}/{month}/{day}/{description}")
    except Repository.NotFound:
        flask.abort(404)

    return flask.render_template(
        'article.pug',
        title=post.title,
        # Day Month Year
        date=post.date.strftime('%d %B %Y'),
        content=markdown.markdown(
            post.content,
            extensions=['fenced_code', 'toc', 'tables'],
        )
    )

@app.errorhandler(404)
def not_found(error: Exception) -> str:
    return flask.render_template('404.pug')