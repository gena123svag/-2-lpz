# Задача 1


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):

        if self.is_available:
            self.is_available = False
            print(f"Книга '{self.title}' выдана.")
        else:
            print(f"Ошибка: книга '{self.title}' уже взята.")

    def return_book(self):
        self.is_available = True
        print(f"Книга '{self.title}' возвращена.")

    def get_info(self):
        status = "Доступна" if self.is_available else "Недоступна"
        return f"{self.title}, {self.author}, {self.year} г. Доступна: {status}"


if __name__ == "__main__":
    book1 = Book("Война и мир", "Лев Толстой", 1867)
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)

    print(book1.get_info())
    print(book2.get_info())
    print("-" * 30)

    book1.borrow()
    print(book1.get_info())
    print("-" * 30)

    book1.borrow()
    print("-" * 30)

    book1.return_book()
    print(book1.get_info())
    print("-" * 30)

    book1.borrow()
    print(book1.get_info())





# Задача 2

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_top(self):
        if not self.students:
            print("В группе нет студентов.")
            return

        best_student = max(self.students, key=lambda s: s.average_grade())
        print(f"Лучший студент в группе '{self.group_name}':")
        print(f"  {best_student.name} — средний балл: {best_student.average_grade():.2f}")


# Проверка
if __name__ == "__main__":
    student1 = Student("Радель")
    student2 = Student("Егор")
    student3 = Student("Адель")

    student1.add_grade(5)
    student1.add_grade(4)
    student1.add_grade(5)
    student1.add_grade(4) 

    student2.add_grade(3)
    student2.add_grade(4)
    student2.add_grade(4) 

    student3.add_grade(5)
    student3.add_grade(5)
    student3.add_grade(5)
    student3.add_grade(4) 

    group = Group("09.02.07-2ВБ")
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    group.show_top()