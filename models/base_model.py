#!/usr/bin/env python3
import uuid
import datetime as dt

class BaseModel():
    
    id = None
    created_at = None
    updated_at = None
    
    def __init__(self, *args, **kwargs) -> None:
        if (kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    setattr(self, key, dt.datetime.fromisoformat(value))
                    print("at created_at")
                    continue
                elif key == "updated_at":
                    setattr(self, key, dt.datetime.fromisoformat(value))
                    continue
                setattr(self, key, value)
            print ("has kwargs")
        else:
            self.id = str(uuid.uuid4())
            self.created_at =  dt.datetime.now()
            self.updated_at =  dt.datetime.now()
            print("doesnt have kwags")
        
    
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
    
    
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

# n = dt.datetime.now()
# m = n.isoformat()
# print(type(m))
# print(m)
# v = dt.datetime.fromisoformat(m)
# print(v)
# print(type(v))


