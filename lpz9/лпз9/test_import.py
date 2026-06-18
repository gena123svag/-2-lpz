"""
Тестирование импорта пакета mypackage.
"""

print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

print("\n1. Импорт пакета:")
import mypackage
print(f"   Версия: {mypackage.__version__}")
print(f"   Доступные компоненты: {mypackage.__all__}")

print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api

print("\n3. Импорт классов и функций:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, validate_age, format_student_info, format_grades
from mypackage.api import APIClient

print("\n✅ Все импорты успешны!")
print("🎉 Пакет mypackage работает корректно!")