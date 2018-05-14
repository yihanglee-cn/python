#coding=utf-8

file_path = 'files\\test.txt'

# with open(file_path) as file:
#     contents = file.read()
#     print(contents.rstrip())

# with open(file_path) as file:
#     for line in file:
#         print(line.rstrip())
#
# with open(file_path) as file:
#     lines = file.readlines()
#     print(lines)
#
# for line in lines:
#     print(line.rstrip())

with open(file_path) as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.strip()
#print(string[:100])
birthday = input('please enter your birthday:')
if birthday in string:
    print("your brthday appears in the pai")
else:
    print("your brithday not appears in the pai")