from file_ import File

class PythonFile(File):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
        
        self.functions = self.extract_functions()

    def extract_functions(self):
        pass

    def execute_file(self):
        exec(self.changed_content)
        
if __name__ == '__main__':
    pf = PythonFile(r'D:\code\dev\python-dev\pi-lang\src\utils\python_file.py')
    pf.split(14, 0)
    pf.write_to_file(r'D:\code\dev\python-dev\pi-lang\src\utils\text.txt')