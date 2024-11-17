import csv

# Данные
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def file_creater(path: str, data: list[dict] = purchases) -> None:
    """Функция для создания данных"""
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(list(purchases[0].keys()))
        for row in purchases:
            writer.writerow(row.values())

    return None


def total_revenue(path: str) -> float:
    """Функция для расчета полной выручки"""
    revenue = 0
    with open(path, "r", encoding="utf-8") as file:
        rows = csv.reader(file)
        rows = list(rows)[1:]
        for item, category, price, quantity in rows:
            revenue += float(price) * float(quantity)

        return revenue


def items_by_category(path: str) -> dict:
    """Функция возвращающая список уникальных товаров в категориях"""
    with open(path, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

        keys = rows[0]

        dict_list = [dict(zip(keys, values)) for values in rows[1:]]

        grouped_data = {}
        for entry in dict_list:
            category = entry["category"]
            item = entry["item"]
            grouped_data.setdefault(category, []).append(item)

    return grouped_data


def expensive_purchases(path: str, min_price=1) -> list[dict]:
    """Функция которая выводит покупки у которых стоимость дороже указанной минималки"""
    with open(path, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

        keys = rows[0]

        dict_list = [dict(zip(keys, values)) for values in rows[1:]]
        purchases = list()

        for entry in dict_list:
            if float(entry["price"]) >= min_price:
                purchases.append(entry)
            else:
                continue

        return purchases


def average_price_by_category(path: str) -> dict:
    """Функция для нахождения средней цены по категориям"""
    with open(path, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    keys = rows[0]

    dict_list = [dict(zip(keys, values)) for values in rows[1:]]

    category_total = {}

    for entry in dict_list:
        if "category" not in entry or "price" not in entry:
            continue

        category = entry["category"]
        try:
            price = float(entry["price"])
        except ValueError:
            continue

        if category not in category_total:
            category_total[category] = {"total_price": 0, "count": 0}

        category_total[category]["total_price"] += price
        category_total[category]["count"] += 1

    average_prices = {
        category: totals["total_price"] / totals["count"]
        for category, totals in category_total.items()
    }

    return average_prices


def most_frequent_category(path: str) -> str:
    """Функция возвращающая в какой категории больше всего покупок"""
    with open(path, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    keys = rows[0]
    dict_list = [dict(zip(keys, values)) for values in rows[1:]]

    category_quantity = {}

    for entry in dict_list:
        if "category" not in entry or "quantity" not in entry:
            continue
        category = entry["category"]

        try:
            quantity = int(entry["quantity"])
        except ValueError:
            continue

        if category not in category_quantity:
            category_quantity[category] = 0

        category_quantity[category] += quantity

    most_frequent = max(category_quantity, key=category_quantity.get)

    return most_frequent

if __name__ == "__main__":
    #file_creater(path: str, data: list[dict] = purchases) # Создаем файл 
    print(f'Общая выручка: {total_revenue('purchases.csv')}')
    print(f'Товары по категориям: {items_by_category('purchases.csv')}')
    print(f'Покупки дороже 1.0: {expensive_purchases('purchases.csv', min_price=1)}')
    print(f'Средняя цена по категориям: {average_price_by_category('purchases.csv')}')
    print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category('purchases.csv')}')
