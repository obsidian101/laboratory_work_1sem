latters = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', "н", 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

try:
    with open('ex2_1.txt', 'w+', encoding='utf-8') as file:
        file.writelines(['— Скажи-ка, дядя, ведь не даром\n','Москва, спаленная пожаром,\n', 'Французу отдана?\n','Ведь были ж схватки боевые,\n','Да, говорят, еще какие!\n', 'Недаром помнит вся Россия\n','Про день Бородина!\n'])
        file.seek(0)

        data = file.read()
        print(data)
        file.seek(0)
        with open('ex2_2.txt', 'w+', encoding='utf-8') as file_3:
            for i in file:
                line = i.split()
                for j in line:
                    if len(line) > 0 and j[0] in latters:
                        file_3.write(j + '\n')
                        file_3.seek(0)
                    print(file_3.readline(),end='')

except:
    print('ошибка')




