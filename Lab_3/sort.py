# sort.py

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

# Блок main уже был в этом задании, он выполняет проверку
if __name__ == "__main__":
    print(f"Исходные данные: {data}\n")

    print("--- Сортировка по модулю (без lambda) ---")
    result = sorted(data, key=abs, reverse=True)
    print(result)

    print("\n--- Сортировка по модулю (с lambda) ---")
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
