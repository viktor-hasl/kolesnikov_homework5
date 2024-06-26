# Viktor Kolesnikov
# Homework-5
# 12-03-2024
# Grodno-IT-Academy-Python 3.11

import re


# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
def get_ranges(lst):
    '''Функция для "сворачивания" списка целых чисел в диапазоны
    '''
    result = []
    # Инициализируем начальное и конечное значения диапазона
    start = end = lst[0]
    # Проходим по списку начиная со второго элемента
    for i in range(1, len(lst)):
        # Если текущий элемент продолжает диапазон обновляем конец диапазона
        if lst[i] == end + 1:
            end = lst[i]
        else:
            # Если диапазон закончился, добавляем его к результату
            if start == end:
                result.append(str(start))
            else:
                # Если начально и конечное число диапазона не равны, то мы сворачиваем диапазон
                # значит у нас несколько чисел в диапазоне
                result.append(f"{start}-{end}")
            start = end = lst[i]
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")
    return ", ".join(result)


# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []
def standardise_phones(*args):
    '''Функция для стандартизации телефонных номеров'''
    result = []
    # Проходим по всем переданным аргументам
    for num in args:
        num = str(num)
        # Удаляем лишние символы из номера
        num = re.sub(r'[ +()-]', '', num)
        # Проверяем на корректность номера
        if len(num) < 9 or re.search(r'[a-z]', num):
            return []
        # Получаем последние 9 цифр номера
        num = re.search(r'\d{9}\b', num).group(0)
        # Добавляем стандартизированный номер к результату
        result.append('+375' + num)
    return result

# Создайте декоратор handle_multiples который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# здесь можно пользоваться циклами
def handle_multiples(func):
    '''Декоратор для обработки множественных ответов'''
    def wrapper(*args):
        lis_num = []
        # Проходим по всем переданным аргументам
        for i in args:
            # на каждый элемент запускаем нашу функцию и добавляем в список
            num = func(i)
            lis_num.append(num)
            # Если передан только один аргумент выводим один элемент
        if len(lis_num) == 1:
            return lis_num[0]
        return lis_num
    return wrapper

# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!

# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54
@handle_multiples
def rope_product(n):
    '''Функция рассчитывает максимальное произведение разбиения числа на меньшие целые числа.
    Подход основан на рекурсии, подход очень плохой, так как программе будет очень долдга искать, я бы тут использовал циклы
    и динамическое программирование
    '''
    # Базовый случай: числа до 4 включительно возвращают сами себя
    if n <= 4:
        return n
    else:
        # Вычисляем максимальное произведение для каждого возможного разбиения числа
        mn = max(2 * rope_product(n-2), 3 * rope_product(n-3), 4 * rope_product(n-4))
    return mn