# unique.py

# Для теста импортируем генератор из предыдущего задания
from gen_random import gen_random


class Unique(object):
    """
    Итератор, который убирает дубликаты из итерируемого объекта.

    Поддерживает опцию ignore_case для строк.
    """

    def __init__(self, items, **kwargs):
        self._items = iter(items)
        self._ignore_case = kwargs.get('ignore_case', False)
        self._seen = set()

    def __next__(self):
        while True:
            i = next(self._items)
            check_item = i
            if self._ignore_case and isinstance(i, str):
                check_item = i.lower()

            if check_item not in self._seen:
                self._seen.add(check_item)
                return i

    def __iter__(self):
        return self


if __name__ == '__main__':
    print("--- Тест Unique с числами ---")
    data1 = [1, 1, 1, 2, 2, 3, 1, 2]
    print(f"Исходные данные: {data1}")
    print("Уникальные:", end=' ')
    for item in Unique(data1):
        print(item, end=' ')
    print("\n")

    print("--- Тест Unique с генератором ---")
    data2_gen = gen_random(15, 1, 5)
    data2_list = list(data2_gen)
    print(f"Исходные данные (случайные): {data2_list}")
    print("Уникальные:", end=' ')
    for item in Unique(data2_list):
        print(item, end=' ')
    print("\n")

    print("--- Тест Unique со строками (ignore_case=False) ---")
    data3 = ['a', 'A', 'b', 'B', 'a', 'A']
    print(f"Исходные данные: {data3}")
    print("Уникальные:", end=' ')
    for item in Unique(data3, ignore_case=False):
        print(item, end=' ')
    print("\n")

    print("--- Тест Unique со строками (ignore_case=True) ---")
    print(f"Исходные данные: {data3}")
    print("Уникальные:", end=' ')
    for item in Unique(data3, ignore_case=True):
        print(item, end=' ')
    print()
