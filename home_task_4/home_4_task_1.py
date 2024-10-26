# 1. 0 - не является натуральным числом,
# поэтому последнее число 10
square_numbers = [_ ** 2 for _ in range(1, 11)]
print(*square_numbers)

# 2. Путь понедельник будет с индексом 1
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_indexes = {key + 1: value for key, value in enumerate(days_of_week)}
print(*days_indexes.items())
# 3 - теги библиотек
libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_libraries = {library.lower() for library in libraries}
print(*tags_libraries)
