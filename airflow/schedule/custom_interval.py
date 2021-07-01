from datetime import datetime

class CustomInterval():
    def __radd__(self, other):
        if not isinstance(other, datetime):
            raise NotImplemented
        return self.next(other)
    
    __add__ = __radd__
        
    def __rsub__(self, other):
        if not isinstance(other, datetime):
            raise NotImplemented
        return self.prev(other)