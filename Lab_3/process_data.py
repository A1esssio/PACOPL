# process_data.py

# Импортируем все необходимые заготовки из предыдущих задач
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique


@print_result
def f1(arg):
    """
    Возвращает отсортированный список уникальных профессий (без учета регистра).
    """
    return sorted(list(Unique(field(arg, "job-name"), ignore_case=True)), key=str.lower)


@print_result
def f2(arg):
    """
    Фильтрует список, оставляя только профессии, начинающиеся со слова "программист".
    """
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    """
    Добавляет к каждой профессии "с опытом Python".
    """
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    """
    Добавляет к каждой профессии случайную зарплату от 100 000 до 200 000 руб.
    """
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{prof}, зарплата {salary} руб." for prof, salary in zip(arg, salaries)]


if __name__ == "__main__":
    mock_data = [
        {"job-name": "Программист Python", "salary": "150000"},
        {"job-name": "Аналитик данных", "salary": "120000"},
        {"job-name": "программист C++", "salary": "180000"},
        {"job-name": "Инженер-программист", "salary": "170000"},
        {"job-name": "Программист Java", "salary": "190000"},
        {"job-name": "Программист Python", "salary": "160000"},  # Дубликат
    ]

    print("--- Запуск цепочки обработки с тестовыми данными ---")
    with cm_timer_1():
        f4(f3(f2(f1(mock_data))))
    print("--- Обработка завершена ---")
