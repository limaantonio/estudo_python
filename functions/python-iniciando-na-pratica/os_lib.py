import os

print(os.path.abspath('../iniciandoPython'))#caminho até chegar nesse arquivo
path_test_file = os.path.abspath('../iniciandoPython/test/folder/test_file.py')
print(os.path.dirname(path_test_file))
print(os.path.exists(path_test_file))
print(os.path.isfile(path_test_file))
print(os.path.isdir(path_test_file))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))