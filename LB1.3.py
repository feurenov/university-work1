sales = [
    {"продукт": "яблука", "кількість": 50, "ціна": 10},
    {"продукт": "банани", "кількість": 20, "ціна": 5},
    {"продукт": "яблука", "кількість": 30, "ціна": 10},
    {"продукт": "груші", "кількість": 10, "ціна": 15}
]

def calculate_revenue(sales_list):
    revenue = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        revenue[product] = revenue.get(product, 0) + total
    return revenue

total_revenue = calculate_revenue(sales)
print("Загальний дохід:", total_revenue)

# Продукти з доходом більше 1000
top_products = [product for product, income in total_revenue.items() if income > 1000]
print("Продукти з доходом більше 1000:", top_products)
