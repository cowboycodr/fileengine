from src.core.utils.expandable_dictionary import ExpandableDictionary
import webbrowser
import pathlib
import os

class File:
    '''
    Editable file tools that can either be 
    overwritten or stored in memory
    '''
    
    def __init__(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            self.__new = True
            with open(filepath, 'a+') as f:
                f.write('')
        else:
            self.__new = False
        
        self.__filepath = os.path.abspath(filepath)
        self.__filepath_url = pathlib.Path(self.__filepath).as_uri()
        
        self.ORIGINAL_CONTENT = self.read_raw_content()
        
        self.content_lines = self.read_lines()
        self.raw_content = self.read_raw_content()
        self.dictionary = self.to_dict()
        self.changed_content = self.read_lines()
        
        self.lines = len(self.content_lines) + 1
        
        self.__file = open(self.__filepath, 'r')
    
    def __repr__(self):
        return f'{self.__class__.__name__}(filepath="{self.__filepath}")'
    
    def __str__(self):
        str_output = []
        
        changed_content_list = self.changed_content.split('\n')
        
        for changed_line in range(0, len(changed_content_list)):
            str_output.append(f'{changed_line + 1}. ' + changed_content_list[changed_line] + '\n')
            
        return ''.join(str_output)

    def is_new(self) -> bool:
        return self.__new

    def get_filepath(self) -> str:
        return self.__filepath

    def delete(self):
        os.remove(self.__filepath)

    def read_raw_content(self) -> str:
        with open(self.__filepath, 'r') as f:
            self.raw_content = f.read()
            
            return self.raw_content
    
    def clear_file(self):
        with open(self.__filepath, 'w') as f:
            pass
    
    def read_lines(self) -> str:
        with open(self.__filepath, 'r') as f:
            content_lines = f.readlines()
            
            self.lines = len(content_lines)
            return content_lines

    def get_line(self, line: int) -> str:
        return self.dictionary[line + 1 ]

    def overwrite(self, filepath: str = None, original: bool = False) -> None:
        '''
        If filepath specified write to other files 
        otherwise writes changes to self
        '''
        
        if not filepath:
            filepath = self.__filepath
            
        with open(filepath, 'w') as f:
            if original:
                f.write(str(self.ORIGINAL_CONTENT))
            else: 
                f.write('\n'.join(self.changed_content))

    def insert(self, line: int, text: str) -> None:
        list_content = self.changed_content
        
        length = len(list_content) - 1
        
        if length < line:
            for _ in range(line - len(list_content)): # adds lines until file long enough to suit given line
                list_content.append('')
                
        list_content.insert(line - 1, str(text))
        
        self.changed_content = list_content

    def remove(self, line: int) -> str:
        list_content = self.changed_content.split("\n")
        
        removed_line = list_content.pop(line - 1)
        
        self.changed_content = "\n".join(list_content)
        
        return removed_line

    def replace(self, line: int, new: str) -> None:
        self.remove(line)
        self.insert(line, new)

    def trim(self, line: int) -> None:
        '''
        Removes lines up until 
        specified line otherwise 
        last line with content
        '''
        
        if line:
            self.changed_content = self.changed_content[:line]

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