import os
import json
import csv
from datetime import datetime, date
from typing import Optional, List, Dict, Any

# ============================================================
# ЧАСТЬ 1: КЛАССЫ (с расширениями для доп. заданий)
# ============================================================

class Logger:
    """Простой логгер для записи действий в файл."""
    LOG_FILE = "library.log"

    @staticmethod
    def log(action: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {action}\n")

class Book:
    """Класс, представляющий книгу (добавлен жанр)."""
    def __init__(self, book_id: int, title: str, author: str, year: int,
                 genre: str = "", copies: int = 1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre          # Доп. задание 1
        self.copies = copies
        self.available = copies

    def is_available(self) -> bool:
        return self.available > 0

    def borrow(self) -> bool:
        if self.is_available():
            self.available -= 1
            return True
        return False

    def return_book(self) -> bool:
        if self.available < self.copies:
            self.available += 1
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "copies": self.copies,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["year"],
            data.get("genre", ""),
            data["copies"]
        )
        book.available = data.get("available", data["copies"])
        return book

    def __str__(self):
        status = "✓" if self.is_available() else "✗"
        genre_str = f" [{self.genre}]" if self.genre else ""
        return f"[{status}] {self.book_id}: {self.title} — {self.author} ({self.year}){genre_str} | {self.available}/{self.copies}"

class Person:
    """Базовый класс для человека."""
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def get_contact_info(self) -> str:
        return f"{self.name} | email: {self.email} | тел: {self.phone}"

    def to_dict(self) -> dict:
        return {"name": self.name, "email": self.email, "phone": self.phone}

class Reader(Person):
    """Класс читателя (наследник Person)."""
    def __init__(self, reader_id: int, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.reader_id = reader_id
        self.borrowed_books = []         # список ID книг
        self.history = []                # история операций (строки)
        # Доп. задание 2: храним даты выдачи
        self.borrow_dates = {}           # book_id -> дата выдачи (строка YYYY-MM-DD)

    def borrow_book(self, book_id: int):
        self.borrowed_books.append(book_id)
        self.borrow_dates[book_id] = date.today().isoformat()
        self.history.append(f"Взял книгу {book_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def return_book(self, book_id: int) -> bool:
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            # Подсчёт дней (доп. задание 2)
            borrow_date = datetime.strptime(self.borrow_dates.pop(book_id), "%Y-%m-%d").date()
            days_held = (date.today() - borrow_date).days
            self.history.append(f"Вернул книгу {book_id} (было {days_held} дн.)")
            return True
        return False

    def has_book(self, book_id: int) -> bool:
        return book_id in self.borrowed_books

    def get_borrowed_count(self) -> int:
        return len(self.borrowed_books)

    def get_borrowed_days(self, book_id: int) -> Optional[int]:
        """Возвращает количество дней, сколько книга у читателя (если ещё на руках)."""
        if book_id in self.borrow_dates:
            borrow_date = datetime.strptime(self.borrow_dates[book_id], "%Y-%m-%d").date()
            return (date.today() - borrow_date).days
        return None

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["reader_id"] = self.reader_id
        data["borrowed_books"] = self.borrowed_books
        data["history"] = self.history
        data["borrow_dates"] = self.borrow_dates
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Reader":
        reader = cls(
            data["reader_id"],
            data["name"],
            data["email"],
            data["phone"]
        )
        reader.borrowed_books = data.get("borrowed_books", [])
        reader.history = data.get("history", [])
        reader.borrow_dates = data.get("borrow_dates", {})
        return reader

    def __str__(self):
        return f"[{self.reader_id}] {self.name} — на руках: {len(self.borrowed_books)} книг"

class Library:
    """Класс, управляющий библиотекой (с расширенными функциями)."""
    def __init__(self, name: str, books_file="data/books.json", readers_file="data/readers.json"):
        self.name = name
        self.books_file = books_file
        self.readers_file = readers_file
        self.books: Dict[int, Book] = {}
        self.readers: Dict[int, Reader] = {}
        self._next_book_id = 1
        self._next_reader_id = 1
        self.load_data()
        Logger.log("Библиотека инициализирована")

    # ---------- ПОИСК ----------
    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id)

    def find_reader_by_id(self, reader_id: int) -> Optional[Reader]:
        return self.readers.get(reader_id)

    def search_books(self, query: str) -> List[Book]:
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or query in book.author.lower() or
                query in book.genre.lower()):
                results.append(book)
        return results

    def search_books_by_genre(self, genre: str) -> List[Book]:
        genre = genre.lower()
        return [b for b in self.books.values() if genre in b.genre.lower()]

    def search_readers(self, query: str) -> List[Reader]:
        query = query.lower()
        return [r for r in self.readers.values() if query in r.name.lower()]

    # ---------- ДОБАВЛЕНИЕ ----------
    def add_book(self, title: str, author: str, year: int, genre: str = "", copies: int = 1) -> Book:
        book = Book(self._next_book_id, title, author, year, genre, copies)
        self.books[self._next_book_id] = book
        self._next_book_id += 1
        self.save_data()
        Logger.log(f"Добавлена книга: {title} (ID {book.book_id})")
        return book

    def add_reader(self, name: str, email: str, phone: str) -> Reader:
        reader = Reader(self._next_reader_id, name, email, phone)
        self.readers[self._next_reader_id] = reader
        self._next_reader_id += 1
        self.save_data()
        Logger.log(f"Добавлен читатель: {name} (ID {reader.reader_id})")
        return reader

    # ---------- ВЫДАЧА И ВОЗВРАТ ----------
    def borrow_book(self, reader_id: int, book_id: int) -> str:
        reader = self.find_reader_by_id(reader_id)
        if not reader:
            return "❌ Читатель не найден"
        book = self.find_book_by_id(book_id)
        if not book:
            return "❌ Книга не найдена"
        if not book.is_available():
            return "❌ Нет доступных экземпляров"
        reader.borrow_book(book_id)
        book.borrow()
        self.save_data()
        Logger.log(f"Выдана книга {book.title} (ID {book_id}) читателю {reader.name} (ID {reader_id})")
        return f"✅ Книга '{book.title}' выдана {reader.name}"

    def return_book(self, reader_id: int, book_id: int) -> str:
        reader = self.find_reader_by_id(reader_id)
        if not reader:
            return "❌ Читатель не найден"
        book = self.find_book_by_id(book_id)
        if not book:
            return "❌ Книга не найдена"
        if not reader.has_book(book_id):
            return "❌ У читателя нет этой книги"
        reader.return_book(book_id)
        book.return_book()
        self.save_data()
        Logger.log(f"Возвращена книга {book.title} (ID {book_id}) от читателя {reader.name}")
        return f"✅ Книга '{book.title}' возвращена"

    # ---------- ОТЧЁТЫ ----------
    def get_all_books(self) -> List[Book]:
        return list(self.books.values())

    def get_all_readers(self) -> List[Reader]:
        return list(self.readers.values())

    def get_available_books(self) -> List[Book]:
        return [b for b in self.books.values() if b.is_available()]

    def get_borrowed_books(self) -> List[Dict]:
        borrowed = []
        for reader in self.readers.values():
            for book_id in reader.borrowed_books:
                book = self.find_book_by_id(book_id)
                if book:
                    days = reader.get_borrowed_days(book_id)
                    borrowed.append({
                        "reader": reader.name,
                        "reader_id": reader.reader_id,
                        "book": book.title,
                        "book_id": book_id,
                        "days_held": days if days is not None else "?"
                    })
        return borrowed

    def get_reader_debtors(self, limit=3) -> List[Reader]:
        return [r for r in self.readers.values() if r.get_borrowed_count() > limit]

    def get_statistics(self) -> Dict:
        return {
            "total_books": len(self.books),
            "total_readers": len(self.readers),
            "available_books": len(self.get_available_books()),
            "borrowed_books": len(self.get_borrowed_books()),
            "debtors": len(self.get_reader_debtors(3))
        }

    # ---------- ЭКСПОРТ В CSV (доп. задание 3) ----------
    def export_books_to_csv(self, filename: str = "reports/books.csv"):
        os.makedirs("reports", exist_ok=True)
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Название", "Автор", "Год", "Жанр", "Всего", "Доступно"])
            for book in self.books.values():
                writer.writerow([book.book_id, book.title, book.author, book.year,
                                 book.genre, book.copies, book.available])
        Logger.log(f"Экспортирован список книг в {filename}")

    def export_readers_to_csv(self, filename: str = "reports/readers.csv"):
        os.makedirs("reports", exist_ok=True)
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "ФИО", "Email", "Телефон", "Книг на руках"])
            for reader in self.readers.values():
                writer.writerow([reader.reader_id, reader.name, reader.email,
                                 reader.phone, reader.get_borrowed_count()])
        Logger.log(f"Экспортирован список читателей в {filename}")

    def export_borrowed_to_csv(self, filename: str = "reports/borrowed.csv"):
        os.makedirs("reports", exist_ok=True)
        borrowed = self.get_borrowed_books()
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Читатель", "ID читателя", "Книга", "ID книги", "Дней на руках"])
            for item in borrowed:
                writer.writerow([item["reader"], item["reader_id"], item["book"],
                                 item["book_id"], item["days_held"]])
        Logger.log(f"Экспортирован список выданных книг в {filename}")

    def export_debtors_to_csv(self, filename: str = "reports/debtors.csv"):
        os.makedirs("reports", exist_ok=True)
        debtors = self.get_reader_debtors(3)
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "ФИО", "Книг на руках"])
            for reader in debtors:
                writer.writerow([reader.reader_id, reader.name, reader.get_borrowed_count()])
        Logger.log(f"Экспортирован список должников в {filename}")

    # ---------- РАБОТА С ФАЙЛАМИ ----------
    def save_data(self):
        os.makedirs("data", exist_ok=True)
        with open(self.books_file, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books.values()], f, ensure_ascii=False, indent=4)
        with open(self.readers_file, "w", encoding="utf-8") as f:
            json.dump([reader.to_dict() for reader in self.readers.values()], f, ensure_ascii=False, indent=4)

    def load_data(self):
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, "r", encoding="utf-8") as f:
                    books_data = json.load(f)
                    max_id = 0
                    for data in books_data:
                        book = Book.from_dict(data)
                        self.books[book.book_id] = book
                        max_id = max(max_id, book.book_id)
                    self._next_book_id = max_id + 1
            except:
                pass
        if os.path.exists(self.readers_file):
            try:
                with open(self.readers_file, "r", encoding="utf-8") as f:
                    readers_data = json.load(f)
                    max_id = 0
                    for data in readers_data:
                        reader = Reader.from_dict(data)
                        self.readers[reader.reader_id] = reader
                        max_id = max(max_id, reader.reader_id)
                    self._next_reader_id = max_id + 1
            except:
                pass

# ============================================================
# ЧАСТЬ 2: КОНСОЛЬНЫЙ ИНТЕРФЕЙС (с расширениями)
# ============================================================

class LibraryApp:
    def __init__(self):
        # Создаём папки при необходимости
        os.makedirs("data", exist_ok=True)
        os.makedirs("reports", exist_ok=True)
        self.lib = Library("Городская библиотека")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title):
        print("\n" + "=" * 60)
        print(f"📚 {title}")
        print("=" * 60)

    def print_menu(self):
        print("\n" + "-" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("-" * 40)
        print("📖 УПРАВЛЕНИЕ КНИГАМИ:")
        print(" 1. Добавить книгу")
        print(" 2. Показать все книги")
        print(" 3. Поиск книг (название/автор/жанр)")
        print(" 4. Поиск по жанру")          # доп. задание 1
        print(" 5. Показать доступные книги")
        print("\n👥 УПРАВЛЕНИЕ ЧИТАТЕЛЯМИ:")
        print(" 6. Добавить читателя")
        print(" 7. Показать всех читателей")
        print(" 8. Поиск читателей")
        print("\n🔄 ОПЕРАЦИИ:")
        print(" 9. Выдать книгу")
        print("10. Вернуть книгу")
        print("11. Книги на руках (с днями)")
        print("\n📊 ОТЧЁТЫ:")
        print("12. Статистика")
        print("13. Должники (>3 книг)")
        print("14. Экспорт отчётов в CSV")   # доп. задание 3
        print("\n💾 ДРУГОЕ:")
        print(" 0. Выход")
        print("-" * 40)

    # ---------- КНИГИ ----------
    def add_book_menu(self):
        self.print_header("ДОБАВЛЕНИЕ КНИГИ")
        title = input("Название: ").strip()
        if not title:
            print("❌ Название не может быть пустым")
            return
        author = input("Автор: ").strip()
        if not author:
            print("❌ Автор не может быть пустым")
            return
        try:
            year = int(input("Год издания: "))
        except ValueError:
            print("❌ Год должен быть числом")
            return
        genre = input("Жанр (оставьте пустым, если не нужен): ").strip()
        try:
            copies = int(input("Количество экземпляров (по умолчанию 1): ") or "1")
        except ValueError:
            copies = 1
        book = self.lib.add_book(title, author, year, genre, copies)
        print(f"\n✅ Книга добавлена: {book}")

    def show_books_menu(self):
        self.print_header("ВСЕ КНИГИ")
        books = self.lib.get_all_books()
        if not books:
            print("📭 В библиотеке нет книг")
            return
        for book in books:
            print(book)

    def search_books_menu(self):
        self.print_header("ПОИСК КНИГ")
        query = input("Введите название, автора или жанр: ").strip()
        if not query:
            print("❌ Введите поисковый запрос")
            return
        results = self.lib.search_books(query)
        print(f"\n🔍 Найдено книг: {len(results)}")
        for book in results:
            print(book)

    def search_by_genre_menu(self):
        self.print_header("ПОИСК ПО ЖАНРУ")
        genre = input("Введите жанр: ").strip()
        if not genre:
            print("❌ Введите жанр")
            return
        results = self.lib.search_books_by_genre(genre)
        print(f"\n🔍 Книги в жанре '{genre}': {len(results)}")
        for book in results:
            print(book)

    def show_available_books_menu(self):
        self.print_header("ДОСТУПНЫЕ КНИГИ")
        books = self.lib.get_available_books()
        if not books:
            print("📭 Нет доступных книг")
            return
        for book in books:
            print(book)

    # ---------- ЧИТАТЕЛИ ----------
    def add_reader_menu(self):
        self.print_header("ДОБАВЛЕНИЕ ЧИТАТЕЛЯ")
        name = input("ФИО: ").strip()
        if not name:
            print("❌ ФИО не может быть пустым")
            return
        email = input("Email: ").strip()
        phone = input("Телефон: ").strip()
        reader = self.lib.add_reader(name, email, phone)
        print(f"\n✅ Читатель добавлен: {reader}")

    def show_readers_menu(self):
        self.print_header("ВСЕ ЧИТАТЕЛИ")
        readers = self.lib.get_all_readers()
        if not readers:
            print("👥 Нет читателей")
            return
        for reader in readers:
            print(reader)

    def search_readers_menu(self):
        self.print_header("ПОИСК ЧИТАТЕЛЕЙ")
        query = input("Введите имя читателя: ").strip()
        if not query:
            print("❌ Введите поисковый запрос")
            return
        results = self.lib.search_readers(query)
        print(f"\n🔍 Найдено читателей: {len(results)}")
        for reader in results:
            print(reader)

    # ---------- ОПЕРАЦИИ ----------
    def borrow_book_menu(self):
        self.print_header("ВЫДАЧА КНИГИ")
        try:
            reader_id = int(input("ID читателя: "))
            book_id = int(input("ID книги: "))
        except ValueError:
            print("❌ ID должны быть числами")
            return
        result = self.lib.borrow_book(reader_id, book_id)
        print(f"\n{result}")

    def return_book_menu(self):
        self.print_header("ВОЗВРАТ КНИГИ")
        try:
            reader_id = int(input("ID читателя: "))
            book_id = int(input("ID книги: "))
        except ValueError:
            print("❌ ID должны быть числами")
            return
        result = self.lib.return_book(reader_id, book_id)
        print(f"\n{result}")

    def show_borrowed_books_menu(self):
        self.print_header("КНИГИ НА РУКАХ (С ДНЯМИ)")
        borrowed = self.lib.get_borrowed_books()
        if not borrowed:
            print("📭 Нет книг на руках")
            return
        for item in borrowed:
            print(f"📖 '{item['book']}' (ID {item['book_id']}) — {item['reader']} (ID {item['reader_id']}) — {item['days_held']} дн.")

    # ---------- ОТЧЁТЫ ----------
    def show_statistics_menu(self):
        self.print_header("СТАТИСТИКА БИБЛИОТЕКИ")
        stats = self.lib.get_statistics()
        print(f"📚 Всего книг:          {stats['total_books']}")
        print(f"📖 Доступно:            {stats['available_books']}")
        print(f"🔄 На руках:            {stats['borrowed_books']}")
        print(f"👥 Читателей:           {stats['total_readers']}")
        print(f"⚠️ Должников (>3 книг):  {stats['debtors']}")
        if stats['total_books'] > 0:
            percent = stats['available_books'] / stats['total_books'] * 100
            print(f"📊 Доступность книг:    {percent:.1f}%")

    def show_debtors_menu(self):
        self.print_header("ДОЛЖНИКИ (>3 КНИГ НА РУКАХ)")
        debtors = self.lib.get_reader_debtors(3)
        if not debtors:
            print("✅ Нет должников")
            return
        for reader in debtors:
            print(f"⚠️ {reader} — книг на руках: {reader.get_borrowed_count()}")

    def export_reports_menu(self):
        self.print_header("ЭКСПОРТ ОТЧЁТОВ В CSV")
        self.lib.export_books_to_csv()
        self.lib.export_readers_to_csv()
        self.lib.export_borrowed_to_csv()
        self.lib.export_debtors_to_csv()
        print("\n✅ Все отчёты сохранены в папку 'reports/'")
        input("Нажмите Enter для продолжения...")

    # ---------- ГЛАВНЫЙ ЦИКЛ ----------
    def run(self):
        self.clear_screen()
        print("=" * 60)
        print("🏫 ДОБРО ПОЖАЛОВАТЬ В БИБЛИОТЕКУ!")
        print(f"   {self.lib.name}")
        print("=" * 60)
        while True:
            self.print_menu()
            choice = input("\nВыберите действие: ").strip()
            if choice == "0":
                print("\n💾 Сохранение данных...")
                self.lib.save_data()
                print("👋 До свидания!")
                Logger.log("Завершение работы приложения")
                break
            # Книги (1-5)
            elif choice == "1":
                self.add_book_menu()
            elif choice == "2":
                self.show_books_menu()
            elif choice == "3":
                self.search_books_menu()
            elif choice == "4":
                self.search_by_genre_menu()
            elif choice == "5":
                self.show_available_books_menu()
            # Читатели (6-8)
            elif choice == "6":
                self.add_reader_menu()
            elif choice == "7":
                self.show_readers_menu()
            elif choice == "8":
                self.search_readers_menu()
            # Операции (9-11)
            elif choice == "9":
                self.borrow_book_menu()
            elif choice == "10":
                self.return_book_menu()
            elif choice == "11":
                self.show_borrowed_books_menu()
            # Отчёты (12-14)
            elif choice == "12":
                self.show_statistics_menu()
            elif choice == "13":
                self.show_debtors_menu()
            elif choice == "14":
                self.export_reports_menu()
            else:
                print("❌ Неверный выбор!")
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    app = LibraryApp()
    app.run()