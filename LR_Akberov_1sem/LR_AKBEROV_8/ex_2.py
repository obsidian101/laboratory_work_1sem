import pickle
text = [
    'строка_1',
    'строка_2',
    1,
    2,
    3,
    4,
    5
]

try:
    with open('ex1_1.bin', 'wb') as file:
        pickle.dump(text, file)

    with open('ex1_1.bin', 'rb') as file:
        data = pickle.load(file)

    with open('ex1_2.bin', 'wb') as new_file:
        for i, s in enumerate(data):
            if i == 1 or (isinstance(s, int) and s % 2 == 0):
                pickle.dump(s,new_file)

    with open('ex1_2.bin', 'rb') as txt_in_new_file:
        while True:
            try:
                data = pickle.load(txt_in_new_file)
                print(data)
            except EOFError:
                break

except:
    print('Проблема')


