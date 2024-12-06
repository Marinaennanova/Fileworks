
""" Задача "Записать и запомнить":

     Создайте функцию custom_write(file_name, strings),
которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.

Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
-1, 2 - номера записанных строк.
-0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.    """


mylist = ["Здраствуйте ,меня зовут Маришка","у меня наступили каникулы","и я собираюсь в поездку на море"]

def custom_write(file_name,mylist): # file_name -название файла, mylist-список строк в нем
    a = 0
    strings_positions = {}# словарь куда будут записываться ключ и его значением,в нашем случае это
    # номер строки,текущей позиции в файле по байту и значение строки
    for i in mylist :
        file = open(file_name,"a",encoding="utf-8")# создание файла smile.txt открытого для записи с кодировкой utf-8
        tell = file.tell() # метод для отслеживания текущей позиции в файле
        a+=1 # нумерация строк
        file.write(f"{i}\n")# запись строк в фаил из сформированного выше списка
        file.close()
        strings_positions.update({(a,tell): i}) # метод формирования словаря с порядковым номером строки,текущая позиция
        # в файле,значение строки(строка из списка)
    return strings_positions

res = custom_write("smile.txt",mylist) # вызов функции где создается фаил с названием и списком

for strings_positions in res.items():# метод возвращающий список кортежа  с парами ключей и их значений
    print(strings_positions)