from dao import StatusDao

from status import Status

class PolicyEngine:
    
    def __init__(self):
        self.status_dao = StatusDao()
        self.status = self.statusDao.read_status()
        
        
    
    
    

statusDao = StatusDao()

statusDao.store_status('{"key": "value"}')

status = statusDao.read_status()

print(status)