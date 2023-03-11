#!/usr/bin/env python3
import sys
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone')

import uuid
import datetime as dt
import models


class BaseModel():

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs) -> None:

        if (kwargs):
            for key, value in kwargs.items():
                tform = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, dt.datetime.strptime(value, tform))
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)

    def __str__(self):
        
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))#40.80

    def save(self):
        self.updated_at = dt.datetime.now()
        models.storage.save()

    def to_dict(self):

        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["created_at"] = self.created_at.isoformat()

        return rdict