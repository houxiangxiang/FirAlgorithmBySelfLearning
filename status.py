class Status:
    
    def __init__(self, value = 0, next_dict = None):
        self.value = value
        self.next_dict = next_dict
        
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
        
    def transform(self, x, y):
        pass
    
    def get_best_next():
        pass
    
    def is_win():
        pass
    
    def update_next(self, next, delta):
        self.next_dict[next] += delta
    
    
    
    