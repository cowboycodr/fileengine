from src.file_engine import FE

if __name__ == '__main__':
    myFile = FE.create(r'D:\code\dev\python-dev\file-engine\kian_mckenna.txt')
    file = FE.grab(myFile.get_filepath())

    file.insert(10, r'\n')
    file.insert(1, 'dog')
    file.overwrite()