inventory = {
    "яблука": 10,
    "банани": 3,
    "груші": 7
}

def update_inventory(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity


update_inventory("яблука", -2)
update_inventory("апельсини", 4)

print("Оновлений інвентар:", inventory)

low_stock = [product for product, qty in inventory.items() if qty < 5]
print("Продукти з низьким залишком:", low_stock)
