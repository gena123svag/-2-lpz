"""
mypackage - пакет для работы с данными о студентах и внешними API.
"""

__version__ = "1.0.0"

from mypackage.models.student import Student
from mypackage.models.group import Group
from mypackage.utils.validators import validate_email, validate_age
from mypackage.utils.formatters import format_student_info, format_grades, format_group_report, print_colored
from mypackage.api.client import APIClient

__all__ = [
    'Student',
    'Group',
    'APIClient',
    'validate_email',
    'validate_age',
    'format_student_info',
    'format_grades',
    'format_group_report',
    'print_colored'
]

print(f"📦 Пакет mypackage версии {__version__} загружен")