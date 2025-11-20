def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for i in items:
            value = i.get(key)
            if value is not None:
                yield value
    else:
        for i in items:
            filtered = {k: v for k, v in i.items() if k in args and v is not None}
            if filtered:
                yield filtered

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print("--- Тест field с одним аргументом ('title') ---")
    for title in field(goods, 'title'):
        print(title)

    print("\n--- Тест field с одним аргументом ('price'), пропуская None ---")
    for price in field(goods, 'price'):
        print(price)

    print("\n--- Тест field с несколькими аргументами ('title', 'price', 'color') ---")
    for item in field(goods, 'title', 'price', 'color'):
        print(item)
