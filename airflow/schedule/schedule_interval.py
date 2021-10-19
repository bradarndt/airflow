import json
from datetime import datetime
from typing import Optional
from pendulum import DateTime

class ScheduleInterval():
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
    
    def skip_to_latest(self, earliest: Optional[DateTime]) -> DateTime:
        """Bound the earliest time a run can be scheduled.

        This is called when ``catchup=False``. 
        """
        raise NotImplementedError()

    def align(self, current: DateTime) -> DateTime:
        """Align given time to the scheduled.

        For fixed schedules (e.g. every midnight); this finds the next time that
        aligns to the declared time, if the given time does not align. If the
        schedule is not fixed (e.g. every hour), the given time is returned.
        """
        raise NotImplementedError()

    def next(self, current: DateTime) -> DateTime:
        """Get the first schedule after the current time."""
        raise NotImplementedError()

    def prev(self, current: DateTime) -> DateTime:
        """Get the last schedule before the current time."""
        raise NotImplementedError()
    
    def __serialize__(self):
        return json.dumps(self.__dict__)
     
    def __deserialize__(cls, s):
        d = json.loads(s)
        return cls(**d)