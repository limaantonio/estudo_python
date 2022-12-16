import os.path

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)
# file = open(BASE_PATH + '/_file_test.dat', 'w') #white
# file.write('school of net')
# file.write('\n')
# file.write('quecia')
# file.close()


# file = open(BASE_PATH + '/_file_test.dat', 'a') #white
# file.write('school of net')
# file.write('\n')
# file.write('quecia')
# file.writelines(('fsdfjasdkf', 'askdjfasdfsdf', 'fsdfjsdkjf'))
# file.writelines(['fsdfjasdkf', 'askdjfasdfsdf', 'fsdfjsdkjf'])
# file.close()

file = open(BASE_PATH + '/_file_test.dat', 'r') #read
#print(file.read())
#print(file.readline())
#print(file.readline(6))
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

