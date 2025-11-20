# gen_random.py

import random

def gen_random(num_count, begin, end):
    """
    Генерирует `num_count` случайных чисел в диапазоне [begin, end].
    """
    for _ in range(num_count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    print("--- Тест gen_random (5 чисел от 1 до 3) ---")
    # Преобразуем генератор в список для вывода
    random_numbers = list(gen_random(5, 1, 3))
    print(random_numbers)

    print("\n--- Тест gen_random (10 чисел от 50 до 100) ---")
    random_numbers_2 = list(gen_random(10, 50, 100))
    print(random_numbers_2)
