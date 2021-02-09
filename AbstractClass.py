from abc import ABC, abstractmethod

class shape(ABC):
    
    @abstractmethod
    def printArea(self):
        pass

class Rectangle(shape):
    pass

