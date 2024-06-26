# Функция для проверки существования файла
import os

def exists(path):
    """Проверяет существует ли файл по указанному пути"""
    return os.path.exists(path) and os.path.isfile(path)
