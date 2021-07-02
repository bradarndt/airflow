import abc
from datetime import datetime

class CustomInterval(abc.ABC):
    def __radd__(self, other):
        if not isinstance(other, datetime):
            raise NotImplemented
        return self.next(other)
    
    __add__ = __radd__
        
    def __rsub__(self, other):
        if not isinstance(other, datetime):
            raise NotImplemented
        return self.prev(other)
    
    def __abs__(self):
        return self
    
    def __str__(self):
        return self.__class__.__name__
    
    @abc.abstractmethod
    def next(self, dttm):
        pass
    
    @abc.abstractmethod
    def prev(self, dttm):
        pass
    
    @abc.abstractmethod
    def __serialize__(self):
        pass
    
    @abc.abstractclassmethod    
    def __deserialize__(cls, s):
        pass