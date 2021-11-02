#!/usr/bin/python3
"""
BASE MODEL
"""
import uuid
import datetime

class BaseModel():
    """
    Base class definition
    """
    def __init__(self, my_number=0):
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.isoformat(datetime.datetime.now())
        self.updated_at = datetime.datetime.isoformat(datetime.datetime.now())

    def __str__(self):
        """ Modify the stdr output with a specific format """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                          self.__dict__)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.isoformat(datetime.datetime.now())

    def to_dict(self):
        """returns a Dictionary with specific attributes """
        """__dict__ returns only set attrinbutes???"""
        traitList = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at']
        printDictionary = {}
        for trait in traitList:
            if trait == "__class__":
                value = str(getattr(self, trait))
                printDictionary[trait] = value[26:-2]
            else:
                printDictionary[trait] = getattr(self, trait)
        return printDictionary