class ExpandableDictionary(dict):
    '''
    A dictionary... but expandable
    '''
    
    def __init__(self) -> None:
        self = dict()
        
    def add(self, key: any, value: any) -> None:
        '''
        add value assigned to name
        '''
        self[key] = value
    
    def add_variable(self, variable) -> None:
        self.add(variable.get_name(), variable)
    
    def remove(self, key: any) -> None:
        del self[key]
        
    def clear(self) -> None:
        self.__init__()