#!/usr/bin/env python3
import json

class FileStorage():
    """cla

    Returns:
        _type_: _description_
    """
    
    __file_path = None
    __object = {}
    
    def __init__(self) -> None:
        pass
    
    def all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__object
    
    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        self.__object = str(obj.__class__.__name__) + str(obj.__class__.id)
        print(self.__object)
        
    def save(self):
        """_summary_
        """
        filename = str(self.__object)
        # with open("")
        saved = json.dumps(self.__object)
        
        
    
    def reload(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if (self.__file_path):
            reloaded_file = json.loads(self.__file_path)
            return reloaded_file
        else:
            pass
        
        
