import json

contacts = []


def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    email = input("Введите email: ")
    group = input("Введите группу: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "group": group
    }

    contacts.append(contact)
    print("Контакт добавлен.")


def find_contact():
    name = input("Введите имя для поиска: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(contact)
            found = True

    if not found:
        print("Контакт не найден.")


def show_group():
    group = input("Введите группу: ")
    found = False

    for contact in contacts:
        if contact["group"].lower() == group.lower():
            print(contact)
            found = True

    if not found:
        print("В этой группе контактов нет.")


def delete_contact():
    name = input("Введите имя для удаления: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Контакт удалён.")
            return

    print("Контакт не найден.")


def save_file():
    filename = input("Введите имя файла: ")
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)
    print("Данные сохранены.")


def load_file():
    global contacts
    filename = input("Введите имя файла: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contacts = json.load(file)
        print("Данные загружены.")
    except FileNotFoundError:
        print("Файл не найден.")


while True:
    print("\nТелефонная книга")
    print("1. Добавить контакт")
    print("2. Поиск по имени")
    print("3. Вывод по группе")
    print("4. Удалить контакт")
    print("5. Сохранить в файл")
    print("6. Загрузить из файла")
    print("7. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        show_group()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        save_file()
    elif choice == "6":
        load_file()
    elif choice == "7":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор.")