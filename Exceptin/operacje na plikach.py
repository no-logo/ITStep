
lines = ['linia 1\n', 'linia 2\n', 'linia 3\n']

file = open('example.txt', 'w')
file.write('zapisujemy do pliku 122\n')
file.write('zapisujemy do pliku 333\n')
file.writelines(lines)
file.close()

file = open('example.txt', 'r')
content = file.read()
file.close()
print(content)

file = open('example.txt', 'r')
lines2 = file.readlines()
file.close()
print(lines2)

try:
    file = open('example.txt', 'w')
    file.write("\ntry finaly\n")
finally:
    file.close()

with open('example.txt', 'w') as file:
    file.writelines(lines)

with open('example.txt', 'r') as file:
    print(f'aktualna pozycja wskaznika {file.tell()}')
    print(f'odczytujemy pierwsy znak {file.read(1)}')
    print(f'aktualna pozycja wskaznika {file.tell()}')

    file.seek(0)
    print(f'aktualna pozycja wskaznika {file.tell()}')
    file.seek(3)
    print(f'odczytujemy pierwsy znak {file.read(1)}')
    print(f'aktualna pozycja wskaznika {file.tell()}')