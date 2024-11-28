
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


with open('example.txt', 'w') as file:
    file.writelines(lines)

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())


with open('example.txt', 'a') as file:
    file.write('nowa linie dopisana do pliku a w trybie append')


with open('example.txt', 'r') as file:
    content = file.read()

print(content)

with open('example.txt', 'r') as file:
    while chunk := file.read(10):
        print(chunk)

    
with open('example.txt', 'w') as file:
    print('sprawdzanie konca pliku.\n')

with open('example.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            print('koniec pliku')
            break

data = b"to jest zapis binarny pliku 2"

with open('example.bin', 'wb') as file:
    file.write(data)

with open('example.bin', 'rb') as file:
    binary_content = file.read()

print(binary_content)

with open('example_truncate.txt', 'w' ) as file:
    file.write('to jest długi plik123 do testowania trycate.')

with open('example_truncate.txt', 'r+' ) as file:
    file.truncate(20)

with open('example_truncate.txt', 'r' ) as file:
    print(file.read())
