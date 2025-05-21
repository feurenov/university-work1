import hashlib

users = {
    "user1": {
        "password": hashlib.md5("pass123".encode()).hexdigest(),
        "name": "Іван Іванович Іваненко"
    },
    "user2": {
        "password": hashlib.md5("secret456".encode()).hexdigest(),
        "name": "Олена Петрівна Сидоренко"
    }
}


def authenticate():
    login = input("Введіть логін: ")

    if login not in users:
        print("❌ Користувача не знайдено.")
        return

    password = input("Введіть пароль: ")
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    if hashed_password == users[login]["password"]:
        print(f"✅ Вітаємо, {users[login]['name']}! Аутентифікація успішна.")
    else:
        print("❌ Невірний пароль.")


authenticate()
