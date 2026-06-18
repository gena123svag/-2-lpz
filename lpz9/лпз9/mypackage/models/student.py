"""
Модуль Student - класс для представления студента.
"""

from datetime import datetime

class Student:
    """
    Класс, представляющий студента.
    """

    _id_counter = 1

    def __init__(self, first_name, last_name, age, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.student_id = f"STU{Student._id_counter:04d}"
        self.grades = []
        self.created_at = datetime.now()
        Student._id_counter += 1

    def add_grade(self, grade, subject="General"):
        if not 2 <= grade <= 5:
            print(f"❌ Ошибка: оценка {grade} должна быть от 2 до 5")
            return False
        self.grades.append({
            'subject': subject,
            'grade': grade,
            'date': datetime.now()
        })
        print(f"✅ Оценка {grade} по {subject} добавлена")
        return True

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(g['grade'] for g in self.grades)
        return total / len(self.grades)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'grades': self.grades,
            'average_grade': self.get_average_grade(),
            'created_at': self.created_at.isoformat()
        }

    def __str__(self):
        return f"Student: {self.get_full_name()} (ID: {self.student_id}, возраст: {self.age})"

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', {self.age})"