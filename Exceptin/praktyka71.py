#zadanie 1
with open(r'C:\Users\User\ITStep\Exceptin\praktyka71.txt', 'r') as file:
    content = file.read().replace('\n','')
    for word in content.split(' '):
        if len(word) > 7:
            print(word)

#zadanie 2
with open(r'C:\Users\User\ITStep\Exceptin\praktyka71.txt', 'r') as file:
    with open(r'C:\Users\User\ITStep\Exceptin\praktyka71_2.txt', 'w') as file2:
        for line in file:
            file2.write(line)

#zadanie 3
with open(r'C:\Users\User\ITStep\Exceptin\praktyka71.txt', 'r') as file:
    with open(r'C:\Users\User\ITStep\Exceptin\praktyka71_3.txt', 'w') as file3:
        for line in reversed(file.readlines()):
            file3.write(line)

#zadanie 4
print('zadanie 4 \n')
with open(r'C:\Users\User\ITStep\Exceptin\praktyka71.txt', 'r+') as file:
    lines = file.readlines()
    print(lines)

    j  = 0
    for i in range(len(lines)):
        if lines[i].find(',') < 0:
            j = i  
    print(j)
    if j == 0:
        j = i + 1         
    lines.insert(j+1,'************\n')  
    print(lines)     
    file.seek(0)
    file.writelines(lines)
 
      
            


