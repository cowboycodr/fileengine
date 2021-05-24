from file_ import File
from expandable_dictionary import ExpandableDictionary

class PythonFile(File):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
        
        self.functions = self.extract_functions()
        
    def extract_functions(self) -> dict:
        raw_functions = self.raw_content.split('DEF'.lower())[1:]
        
        functions = ExpandableDictionary()
        function_details = ExpandableDictionary()
        
        for function in raw_functions:
            function_name = function.split('(')[0].replace(' ', '')
            function_args = function.split('(')[1].split(')')[0].split(',')
            function_code = function.split('\n')[1:]
            
            function_details.add('name', function_name)
            function_details.add('args', function_args)
            function_details.add('content', function_code)
            
            functions.add(function_name, function_details)
            
        return functions
        
if __name__ == '__main__':
    pf = PythonFile(r'src\core\python_types\function_extraction_test.py')
    
    print(pf.functions)