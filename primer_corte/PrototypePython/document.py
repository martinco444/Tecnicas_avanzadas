from abc import ABC, abstractmethod

# Interfaz Document
class Document(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def print(self):
        pass
