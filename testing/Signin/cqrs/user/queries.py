from typing import List
from model.data.gino_model import User

class UserListQuery:

    def __init__(self): 
        self._records:List[User] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

class UserRecordQuery: 
    
    def __init__(self): 
        self._record:User = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record