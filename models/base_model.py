#!/usr/bin/env python3
import uuid
import datetime as dt

class BaseModel():
    
    id = 0
    created_at = 0
    updated_at = 0
    
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at =  dt.datetime.now()
        self.updated_at =  dt.datetime.now()
        
    
    def __str__(self):
        
        return ("[{}] {} {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        self.updated_at = dt.datetime.now()
        
    def to_dict(self):
        
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["created_at"] = self.created_at.isoformat()
        return rdict
    
