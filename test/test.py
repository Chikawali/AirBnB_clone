from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

house = BaseModel()
my_house = house.to_dict()
print(my_house)

