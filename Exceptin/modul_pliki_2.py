with open(r'C:\Users\User\ITStep\Exceptin\modul_pliki_2_brzydkie_slowa.txt', 'r') as file_brzydkie_slowa:
    lines = [i.replace('\n', '') for i in file_brzydkie_slowa.readlines()]

with open(r'C:\Users\User\ITStep\Exceptin\modul_pliki_2_usun_brzydkie_slowa.txt', 'r+') as file1:
    content = file1.read()
    print(content)
    for word in lines:
        content = content.replace(word, '')

    file1.truncate(0)
    file1.seek(0)
    file1.write(content)
            

   