from src.core.utils.expandable_dictionary import ExpandableDictionary

class Variable:
    '''
    Basic variable class
    
    Capable of recording and accessing all value
    changes
    '''
    
    def __init__(self, name: str, value: any):
        self.__name = name
        self.__current_value = value
        
        self.__value_changes = [self.__current_value]
        
        self.dictionary = self.to_dict()
        
    def __str__(self):
        return str(self.__current_value)
    
    def set_value(self, new_value: any):
        if new_value != self.__current_value:
            self.__current_value = new_value
            self.__value_changes.append(new_value)
            
    def get_value(self) -> any:
        return self.__current_value
    
    def get_value_changes(self) -> list:
        return self.__value_changes
    
    def to_dict(self) -> dict:
        values = ExpandableDictionary()
        
        for value_index in range(len(self.__value_changes)):
            value_dict = ExpandableDictionary()
            
            value_type = str(type(self.__value_changes[value_index])).replace("<class '", '').replace("'>", "")
            value = self.__value_changes[value_index]
            
            value_dict.add('value', value)
            value_dict.add('type', value_type)
            
            if value_index == 0:
                values.add('original', value_dict)
                
            values.add(value_index, value_dict)
            
        self.dictionary = values
        
        return values

    def get_name(self) -> str:
        return self.__name
  
        return values
            