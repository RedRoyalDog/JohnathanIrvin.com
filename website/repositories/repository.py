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
from typing import Protocol

from website.models.entity import Entity


class Repository(Protocol):
    def create(self, model: Entity) -> Entity:
        """
        Creates a new entity.

        Args:
            model (Entity): The entity to create.

        Returns:
            Entity: The created entity.
        """        
        ...

    def update(self, identifier: str | int, model: Entity) -> Entity:
        """
        Updates an existing entity.

        Args:
            identifier (str | int): The identifier of the entity to update.
            model (Entity): The entity to update.

        Returns:
            Entity: The updated entity.
        """        
        ...

    def delete(self, identifier: str | int) -> Entity:
        """
        Deletes an existing entity.

        Args:
            identifier (str | int): The identifier of the entity to delete.

        Returns:
            Entity: The deleted entity.
        """        
        ...

    def get(self, identifier: str | int) -> Entity:
        """
        Gets an existing entity.

        Args:
            identifier (str | int): The identifier of the entity to get.

        Returns:
            Entity: The entity.
        """        
        ...

    def get_all(self) -> list:
        """
        Gets all existing entities.

        Returns:
            list: The entities.
        """        
        ...