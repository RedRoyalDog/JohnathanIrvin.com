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
import io
import os
import random

import flask
import markdown
from flask_talisman import Talisman

from website.repositories import (Repository, blog_repositories,
                                  image_repositories)

app = flask.Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'cdn.jsdelivr.net',
        'googletagmanager.com',
        'www.googletagmanager.com',
        'google-analytics.com',
        'www.google-analytics.com',
    ]
}
Talisman(app, content_security_policy=csp)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

blog_repo = blog_repositories.PostRepository('blog')
image_repo = image_repositories.ImageRepository('images')

@app.route('/')
def index() -> str:
    """
    Render the index page.

    Returns:
        str: The rendered index page.
    """    
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
    return flask.render_template(
        'images.pug',
        images=image_repo.get_all()
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
    image = image_repo.get(name)

    if image is None:
        flask.abort(404)

    mimetype = 'image/jpeg' if image.extension == 'jpg' else 'image/png'

    return flask.Response(
        image.content,
        mimetype=mimetype,
    )

@app.route('/images/<string:name>/thumbnail')
def image_thumbnail(name: str) -> str:
    """
    Returns the image with the given name.

    Args:
        name: The name of the image.
    
    Returns:
        str: The rendered template.
    """

    image = image_repo.get(name)

    if image is None:
        flask.abort(404)

    mimetype = 'image/jpeg' if image.extension == 'jpg' else 'image/png'
    format = 'JPEG' if image.extension == 'jpg' else 'PNG'

    img_io = io.BytesIO()
    image.thumbnail(200).save(img_io, format, quality=70)
    img_io.seek(0)

    return flask.send_file(
        img_io,
        mimetype=mimetype,
    )

@app.route('/articles/<int:year>/<int:month>/<int:day>/<string:description>')
def article(year: int, month: int, day: int, description: str) -> str:
    """
    Returns the article with the given description.

    Args:
        year (int): The year of the article.
        month (int): The month of the article.
        day (int): The day of the article.
        description (str): The description of the article.

    Returns:
        str: The rendered template.
    """    
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
    """
    Returns the RSS feed.

    Returns:
        str: The rendered template.
    """    
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
    """
    Returns a sitemap of the website.

    Returns:
        str: The rendered template.
    """    
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


@app.route('/favicon')
@app.route('/favicon.ico')
def favicon() -> flask.Response:
    """
    Returns a random favicon from the static -> favicons directory.

    Returns:
        flask.Response: The image response.
    """
    directory = os.path.join(
        app.root_path,
        'static',
        'icons',
    )
    images = os.listdir(directory)
    image = random.choice(images)

    return flask.send_from_directory(
        directory,
        image,
    )

with open('website/static/faq.md', 'r') as file:
    QUESTION_MARKDOWN = file.read()
@app.route('/faq')
def faq() -> str:
    """
    Returns the FAQ page.

    Returns:
        str: The rendered template.
    """
    return flask.render_template(
        'faq.pug',
        content=markdown.markdown(
            QUESTION_MARKDOWN,
            extensions=['fenced_code', 'toc', 'tables'],
        )
    )

@app.errorhandler(404)
def not_found(error: Exception) -> str:
    """
    Returns the 404 page.

    Returns:
        str: The rendered template.
    """    
    return flask.render_template('404.pug'), 404
