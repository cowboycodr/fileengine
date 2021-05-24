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
            function_code = function.split('\n')[1:]
            
            raw_function_args = function.split('(')[1].split(')')[0].split(',')
            function_args = ExpandableDictionary()
            for arg in raw_function_args:
                arg = arg.split(':')[0] + ' =' + arg.split('=')[1]
                
                arg_name = arg.split('=')[0].replace(' ', '')
                arg_value = arg.split('=')[1][1:]
                
                function_args.add(arg_name, arg_value)
            
            function_details.add('name', function_name)
            function_details.add('args', function_args)
            function_details.add('content', function_code)
            
            functions.add(function_name, function_details)
            
        return functions

    def execute_function(self, function_template, *args): #use: pr.execute_function('do_nothing(nothing, this)), 'nothing', 'this')
        function_reference = self.functions[function_template.split('(')[0].replace(' ', '')]
        
        print(function_reference)
        
        #TODO: Parse args and replace with given values

    def execute_file(self) -> bool:
        try:
            exec(self.raw_content)
            return True
        except:
            return False
     
if __name__ == '__main__':
    pf = PythonFile(r'src\core\python_types\function_extraction_test.py')
    
    pf.execute_function('do_nothing()')