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
from dataclasses import dataclass

import PIL.Image
import io

@dataclass
class Image:
    title: str
    content: bytes

    @property
    def extension(self) -> str:
        return self.title.split('.')[-1]

    def thumbnail(self, size: int) -> PIL.Image.Image:
        """
        Returns a thumbnail of the image.

        Args:
            size (int): The size of the thumbnail.

        Returns:
            PIL.Image.Image: The thumbnail of the image.
        """
        image = PIL.Image.open(io.BytesIO(self.content))
        image.thumbnail((size, size))
        return image

    def get_identifier(self) -> str:
        """
        Returns the identifier of the image.

        Returns:
            str: The identifier of the image.
        """
        return self.title
