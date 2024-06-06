from typing import List
from model.data.gino_model import Campaign

class CampaignListQuery:

    def __init__(self): 
        self._records:List[Campaign] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

class CampaignRecordQuery: 
    
    def __init__(self): 
        self._record:Campaign = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record