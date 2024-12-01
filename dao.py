import json

class StatusDao:
    def __init__(self, file_name = "status.json"):
        self.file_name = file_name
        
    def read_status(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)
    
    def store_status(self, status):
        with open(self.file_name, 'w') as f:
            json.dump(status, f, indent=4)