import os
file_name = ''
content = set()
path = r'C:\Users\User\ITStep\Exceptin\f.txt'

while file_name !='q':
    file_name = input('podaj nazwe pliku: ')
    if file_name != 'q':
        with open(path.replace('f.txt', file_name), 'r') as file:
            content = file.read()

print(content)