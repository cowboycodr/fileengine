class ExpandableDictionary(dict):
    '''
    A dictionary... but expandable
    '''
    
    def __init__(self) -> None:
        self = dict()
        
    def add(self, key: any, value: any) -> None:
        self[key] = value
        
    def remove(self, key: any) -> None:
        del self[key]