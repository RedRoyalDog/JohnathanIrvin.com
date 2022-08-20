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
import os

import flask
import markdown

from website.repositories import Repository, blog_repositories

app = flask.Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
blog_repo = blog_repositories.PostRepository('blog')

@app.route('/')
def index() -> str:
    return flask.render_template(
        'index.pug',
        posts=sorted(
            blog_repo.get_all(),
            key=lambda post: post.date,
            reverse=True,
        )
    )

@app.route('/images')
def images() -> str:
    """
    Returns a list of all images in the images directory.

    Returns:
        str: The rendered template.
    """    
    images = []
    directory = os.path.join('website', 'images')

    for image in os.listdir(directory):
        images.append(image.replace(' ', '_'))
    
    return flask.render_template(
        'images.pug',
        images=images
    )

@app.route('/images/<string:name>')
def image(name: str) -> str:
    """
    Returns the image with the given name.

    Args:
        name: The name of the image.
    
    Returns:
        str: The rendered template.
    """ 
    return flask.send_from_directory(
        "images",
        name.lower().replace('_', ' ')
    )

@app.route('/articles/<int:year>/<int:month>/<int:day>/<string:description>')
def article(year: int, month: int, day: int, description: str) -> str:
    try:
        post = blog_repo.get(f"{year}/{month}/{day}/{description}")
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

@app.route('/rss.xml')
@app.route('/feed.xml')
@app.route('/rss')
@app.route('/feed')
def rss() -> str:
    sorted_items = sorted(
        blog_repo.get_all(),
        key=lambda post: post.date,
        reverse=True,
    )
    response = flask.make_response(
        flask.render_template(
            'rss.xml',
            title='Johnathan Irvin',
            description='Engineer, Researcher, Entrepreneur',
            link='https://johnathanirvin.com',
            lastBuildDate=sorted_items[0].date,
            items=sorted_items,
        )
    )
    response.mimetype = 'application/xml'
    return response

@app.route('/sitemap.xml')
@app.route('/sitemap')
def sitemap() -> str:
    sorted_items = sorted(
        blog_repo.get_all(),
        key=lambda post: post.date,
        reverse=True,
    )
    response = flask.make_response(
        flask.render_template(
            'sitemap.xml',
            items=sorted_items,
        )
    )
    response.mimetype = 'application/xml'
    return response

@app.errorhandler(404)
def not_found(error: Exception) -> str:
    return flask.render_template('404.pug')
