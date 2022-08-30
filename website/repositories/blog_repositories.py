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

import frontmatter
import website.repositories.errors as errors
from website.models.blog import Post


class PostRepository:
    def _get_path(self, model: Post) -> str:
        """
        Gets the path of a post.

        Args:
            model (Post): The post to get the path of.

        Returns:
            str: The path of the post.
        """        
        return os.path.join(
            self._dir,
            str(model.date.year),
            model.description.lower().replace(' ', '-'),
        )

    def _load_posts(self, directory: str) -> dict[str, Post]:
        """
        Loads all posts from the given directory and child directories.

        Args:
            directory (str): The directory to load posts from.

        Returns:
            dict[str, Post]: The loaded posts.
        """
        posts = {}
        directory = os.path.join('website', directory)
        for root, _, files in os.walk(directory):
            for file in files:
                if not file.endswith('.md'):
                    continue

                with open(os.path.join(root, file), 'r') as f:
                    metadata, content = frontmatter.parse(f.read())
                    post = (
                        Post(
                            **metadata,
                            content=content,
                        )
                    )
                    posts[post.get_identifier()] = post

                    
        return posts

    def __init__(self, directory: str = 'blog'):
        """
        Initializes a new instance of the PostRepository class.

        Args:
            directory (str, optional): The directory to load posts from. Defaults to './blog'.
        """
        self._dir = directory
        self._posts: dict[str, Post] = self._load_posts(directory)

    def create(self, model: Post) -> Post:
        """
        Creates a new post.

        Args:
            model (Post): The post to create.

        Returns:
            Post: The created post.
        """
        header = {
            key: value
            for key, value in
            model.__dict__.items()
            if key not in ['content']
        }
        path = self._get_path(model)
        if os.path.exists(path):
            raise errors.EntityAlreadyExists()

        with open(path, 'w') as f:
            f.write(frontmatter.dumps(header))
            f.write(model.content)

        return model

    def update(self, identifier: str, model: Post) -> Post:
        """
        Updates an existing post.

        Args:
            identifier (str): The identifier of the post to update.
            model (Post): The post to update.

        Returns:
            Post: The updated post.
        """
        model = self._posts.get(identifier, None)
        if model is None:
            raise errors.EntityNotFound()
        
        header = {
            key: value
            for key, value in
            model.__dict__.items()
            if key not in ['content']
        }

        with open(self._get_path(model), 'w') as f:
            f.write(frontmatter.dumps(header))
            f.write(model.content)

        return model

    def delete(self, identifier: str) -> Post:
        """
        Deletes a post by its identifier.

        Args:
            identifier (str): The identifier of the post to delete.

        Returns:
            Post: The deleted post.
        """        
        os.remove(self._get_path(self._posts[identifier]))
        del self._posts[identifier]
        return self._posts[identifier]

    def get(self, identifier: str) -> Post:
        """
        Gets a post by its identifier.

        Args:
            identifier (str): The identifier of the post to get.

        Returns:
            Post: The post.
        """
        post = self._posts.get(identifier, None)
        if post is None:
            raise errors.EntityNotFound()

        return post

    def get_all(self) -> list[Post]:
        """
        Gets all posts.

        Returns:
            list[Post]: The posts.
        """
        return list(self._posts.values())
