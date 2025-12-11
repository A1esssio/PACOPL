# print_result.py

from functools import wraps


def print_result(func):
    """
    Декоратор, который печатает имя функции и ее результат.
    Форматирует вывод для списков и словарей.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)

        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)

        return result

    return wrapper


# Блок main для проверки декоратора
if __name__ == "__main__":

    @print_result
    def test_1():
        return 1

    @print_result
    def test_2():
        return "iu5"

    @print_result
    def test_3():
        return {"a": 1, "b": 2}

    @print_result
    def test_4():
        return [1, 2]

    print("--- Запуск тестов для декоратора print_result ---\n")
    test_1()
    print("-" * 20)
    test_2()
    print("-" * 20)
    test_3()
    print("-" * 20)
    test_4()
    print("\n--- Тесты завершены ---")
