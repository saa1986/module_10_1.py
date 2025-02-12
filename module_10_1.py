""" Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков
Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время"""
#
import time  # Импортируем модуль time для работы с временем
from threading import Thread  # Импортируем класс Thread из модуля threading для работы с потоками
from time import sleep  # Импортируем функцию sleep для добавления задержек
from datetime import datetime  # Импортируем класс datetime для работы с датой и временем


def write_words(word_count, file_name):
    """
    Функция для записи заданного количества строк в файл.

    :param word_count: Количество записываемых строк
    :param file_name: Название файла, в который будут записываться строки
    """
    with open(file_name, 'w') as file:  # Открываем файл для записи (создаем новый файл или перезаписываем существующий)
        for i in range(1, word_count + 1):  # Цикл от 1 до word_count (включительно)
            file.write(f"Какое-то слово № {i}\n")  # Записываем строку в файл с номером слова
            sleep(0.1)  # Пауза на 0.1 секунды после каждой записи
    print(f"Завершилась запись в файл {file_name}")  # Сообщаем о завершении записи в файл


start_time = datetime.now()  # Запоминаем текущее время перед выполнением функций
write_words(10, "example1.txt")  # Вызов функции для записи 10 строк в example1.txt
write_words(30, "example2.txt")  # Вызов функции для записи 30 строк в example2.txt
write_words(200, "example3.txt")  # Вызов функции для записи 200 строк в example3.txt
write_words(100, "example4.txt")  # Вызов функции для записи 100 строк в example4.txt
print(f"Работа функций {datetime.now() - start_time}")  # Выводим время, затраченное на выполнение функций

start_time = datetime.now()  # Запоминаем текущее время перед запуском потоков
threads = []  # Создаем пустой список для хранения потоков
# Создаем список аргументов для потоков
for i in [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]:
    thread = Thread(target=write_words, args=i)  # Создаем новый поток с целью вызвать функцию write_words с аргументами
    threads.append(thread)  # Добавляем созданный поток в список потоков
    thread.start()  # Запускаем поток

for thread in threads:  # Цикл по всем созданным потокам
    thread.join()  # Ожидаем завершения каждого потока

print(f"Работа потоков {datetime.now() - start_time}")  # Выводим время, затраченное на выполнение потоков