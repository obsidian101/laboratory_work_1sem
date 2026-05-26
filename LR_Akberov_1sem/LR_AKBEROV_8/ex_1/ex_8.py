import io
from urllib.request import urlopen

def read_all(reader):
    while True:
        ch = reader.read(1)
        if not ch:
            break
        print(ch, end='')
    print("\n конец")

try:
    # Файл с кодировкой cp1251
    with open("MyFile1.txt", "rb") as f:
        text = f.read().decode("cp1251")
        read_all(io.StringIO(text))

    # Интернет-страница (UTF-8)
    with urlopen("http://example.com") as u:
        text = u.read().decode("utf-8")
        read_all(io.StringIO(text))

    # Массив байт
    arr = bytes([5, 8, 3, 9, 11])
    read_all(io.StringIO(arr.decode("cp1251", errors="ignore")))

except Exception as e:
    print("Ошибка:", e)