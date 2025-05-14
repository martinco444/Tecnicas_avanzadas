from abc import ABC, abstractmethod
import copy
from typing import Dict

from document import Document

# Clase abstracta que implementa la interfaz Document
class AbstractDocument(Document):
    def __init__(self):
        self.author = None
        self.creation_date = None
        self.title = None

    # Constructor prototipo
    def __init_copy__(self, source=None):
        if source:
            self.author = source.author
            self.creation_date = source.creation_date
            self.title = source.title

    # Getters y setters
    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_creation_date(self):
        return self.creation_date

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def print(self):
        pass