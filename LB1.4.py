tasks = {
    "Підготувати звіт": "в процесі",
    "Зустріч з клієнтом": "очікує",
    "Оновити сайт": "виконано"
}

def add_task(name, status="очікує"):
    tasks[name] = status

def delete_task(name):
    if name in tasks:
        del tasks[name]

def update_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status

add_task("Написати статтю")
update_status("Підготувати звіт", "виконано")
delete_task("Оновити сайт")

print("Поточні задачі:", tasks)

pending_tasks = [task for task, status in tasks.items() if status == "очікує"]
print("Задачі в очікуванні:", pending_tasks)
