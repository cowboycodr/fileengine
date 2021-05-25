from file_ import File
from expandable_dictionary import ExpandableDictionary

class PythonFile(File):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
        
        self.functions = self.extract_functions()
        self.variables = self.extract_variables()
    
    def extract_functions(self) -> dict:
        raw_functions = self.raw_content.split('DEF'.lower())[1:]
        
        functions = ExpandableDictionary()
        function_details = ExpandableDictionary()
        
        for function in raw_functions:
            function_name = function.split('(')[0].replace(' ', '')
            function_code = function.split('\n')[1:]
            function_code_dict = ExpandableDictionary()
            function_variables = self.extract_variables(function_code)

            for function_line in range(len(function_code)):
                function_code_dict.add(function_line, function_code[function_line])
            
            raw_function_args = function.split('(')[1].split(')')[0].split(',')
            function_args = ExpandableDictionary()
            for arg in raw_function_args:
                try:
                    arg = arg.split(':')[0] + ' =' + arg.split('=')[1]
                
                    arg_name = arg.split('=')[0].replace(' ', '')
                    arg_value = arg.split('=')[1][1:]
                except IndexError:
                    arg_name = arg
                    arg_value = 'None'
                
                function_args.add(arg_name, arg_value)
            
            function_details.add('name', function_name)
            function_details.add('args', function_args)
            function_details.add('content', function_code)
            function_details.add('content-dict', function_code_dict)
            function_details.add('varirables', function_variables)

            functions.add(function_name, function_details)
            
            function_details = ExpandableDictionary()
            function_args = ExpandableDictionary()

        return functions

    def extract_variables(self, content_lines: list = None) -> dict:
        raw_variables = ExpandableDictionary()

        if not content_lines:
            content_lines = self.content_lines

        for line in content_lines:
            if line.count('=') == 1 and line.count('DEF'.lower()) == 0:
                variable_name = line.split('=')[0].replace(' ', '')

                variable_value = line.split('=')[1]

                if variable_value[0] == ' ':
                    variable_value = variable_value[1:]

                raw_variables.add(variable_name, variable_value)

        return raw_variables

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