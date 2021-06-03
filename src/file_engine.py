from src.core.file_ import File

class FileEngine:
    def __init__(self):
        pass
    
    def grab(self, filepath: str):
        '''
        Returns instance of 
        given filepath if possible
        '''
        
        file = File(filepath)
        
        if file.is_new():
            file.delete()
            
            return False
        else:
            return file
    
    def create(self, filepath: str, file_type: str = 'txt'):
        '''
        Creates and returns and instance of a file
        '''
        
        if not filepath.endswith(f'.{file_type}'):
            filepath += f'.{file_type}'
        
        return File(filepath)
    
FE = FileEngine()