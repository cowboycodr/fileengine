from expandable_dictionary import ExpandableDictionary

class File:
    '''
    Editable file tools that can either be 
    overwritten or stored in memory
    '''
    
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        
        self.ORIGINAL_CONTENT = self.read_raw_content()
        
        self.content_lines = self.read_lines()
        self.raw_content = self.read_raw_content()
        self.dictionary = self.to_dict()
        self.changed_content = self.read_raw_content()
        
        self.lines = len(self.content_lines) + 1
    
    def __repr__(self):
        return f'{self.__class__.__name__}(filepath="{self.filepath}")'
    
    def __str__(self):
        return self.changed_content

    def read_raw_content(self) -> str:
        with open(self.filepath, 'r') as f:
            self.raw_content = f.read()
            
            return self.raw_content
    
    def clear_file(self):
        with open(self.filepath, 'w') as f:
            pass
    
    def read_lines(self) -> str:
        with open(self.filepath, 'r') as f:
            return f.readlines()

    def get_line(self, line: int) -> str:
        return self.dictionary[line + 1 ]

    def write_to_file(self, filepath: str = None, original: bool = False) -> None:
        '''
        If filepath specified write to other files 
        otherwise writes changes to self
        '''
        
        if not filepath:
            filepath = self.filepath
            
        with open(filepath, 'w') as f:
            if original:
                f.write(str(self.ORIGINAL_CONTENT))
            else: 
                f.write(''.join(self.changed_content))

    def insert(self, line: int, text: str) -> None:
        list_content = self.changed_content.split("\n")
              
        list_content.insert(line - 1, text)
        
        self.changed_content = "\n".join(list_content)

    def remove(self, line: int) -> str:
        list_content = self.changed_content.split("\n")
        
        removed_line = list_content.pop(line - 1)
        
        self.changed_content = "\n".join(list_content)
        
        return removed_line

    def replace(self, line: int, new: str) -> None:
        self.remove(line)
        self.insert(line, new)

    def move_line(self, line: int, new_line: int) -> None:
        removed_line = self.remove(line)
        self.insert(new_line, removed_line)

    def swap_lines(self, line_1: int, line_2: int) -> None:
        self.move_line(line_1, line_2)
        self.move_line(line_2, line_2)

    def split(self, line: int, side: int = 0) -> list:
        values = list(self.dictionary.values())
        
        if side == 0:
            changed_content = values[:line - 1]
            self.changed_content = changed_content
            
            return changed_content
        else:
            changed_content = values[line - 1:]
            self.changed_content = changed_content
            
            return changed_content
   
    def to_dict(self) -> dict:
        line_count = 1
        
        dictionary = ExpandableDictionary()
        
        for line in self.read_lines():
            dictionary.add(line_count, line)
            line_count += 1
            
        return dictionary