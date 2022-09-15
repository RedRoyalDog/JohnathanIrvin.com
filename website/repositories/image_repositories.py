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
import datetime
import os

import website.repositories.errors as errors
from website.models.image import Image


class ImageRepository:
    def _get_path(self, model: Image) -> str:
        """
        Gets the path of a image.

        Args:
            model (Image): The image to get the path of.

        Returns:
            str: The path of the image.
        """        
        return os.path.join(
            self._dir,
            model.get_identifier()
        )

    def _load_images(self, directory: str) -> dict[str, Image]:
        """
        Loads all images from the given directory and child directories.

        Args:
            directory (str): The directory to load images from.

        Returns:
            dict[str, Image]: The loaded images.
        """
        posts = {}
        directory = os.path.join('website', directory)
        for _, _, files in os.walk(directory):
            for file in files:
                if not file.endswith('.jpg') and not file.endswith('.png'):
                    continue
                
                with open(os.path.join(directory, file), 'rb') as f:
                    content = f.read()
                    created = os.path.getctime(os.path.join(directory, file))
                    image = Image(
                        title=file,
                        created=datetime.datetime.fromtimestamp(created),
                        content=content,
                    )
                    posts[image.get_identifier()] = image
        
        return posts

    def __init__(self, directory: str = 'images'):
        """
        Initializes a new instance of the ImageRepository class.

        Args:
            directory (str, optional): The directory to load images from. Defaults to './images'.
        """
        self._dir = directory
        self._images: dict[str, Image] = self._load_images(directory)

    def create(self, model: Image) -> Image:
        """
        Creates a new image.

        Args:
            model (Image): The image to create.

        Raises:
            EntityAlreadyExists: If the image already exists.

        Returns:
            Image: The created image.
        """
        path = self._get_path(model)
        if os.path.exists(path):
            raise errors.EntityAlreadyExists()

        with open(path, 'w') as f:
            f.write(model.content)

        return model

    def update(self, identifier: str, model: Image) -> Image:
        """
        Updates an existing image.

        Args:
            identifier (str): The identifier of the image to update.
            model (Image): The image to update.

        Raises:
            EntityNotFound: If the image does not exist.

        Returns:
            Image: The updated image.
        """
        model = self._images.get(identifier, None)
        if model is None:
            raise errors.EntityNotFound()

        with open(self._get_path(model), 'w') as f:
            f.write(model.content)

        return model

    def delete(self, identifier: str) -> Image:
        """
        Deletes a image by its identifier.

        Args:
            identifier (str): The identifier of the image to delete.

        Returns:
            Image: The deleted image.
        """        
        os.remove(self._get_path(self._images[identifier]))
        del self._images[identifier]
        return self._images[identifier]

    def get(self, identifier: str) -> Image:
        """
        Gets a image by its identifier.

        Args:
            identifier (str): The identifier of the image to get.

        Raises:
            EntityNotFound: If the image does not exist.

        Returns:
            Image: The image.
        """
        model = self._images.get(identifier, None)
        if model is None:
            raise errors.EntityNotFound()

        return model

    def get_all(self) -> list[Image]:
        """
        Gets all images.

        Returns:
            list[Image]: The images.
        """
        return list(self._images.values())
