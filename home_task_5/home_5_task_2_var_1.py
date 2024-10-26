import os
from datetime import datetime
import black

current_date = datetime.now().strftime('%Y-%m-%d')
base_dir = os.path.join(os.getcwd(), current_date)
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
else:
    print(f"Директория {base_dir} уже существует")

file_path = os.path.join(base_dir, 'empty.txt')

if not os.path.exists(file_path):
    with open(file_path, 'w'):
        print(f"Файл {file_path} создан.")
else:
    print(f"Файл {file_path} уже существует")

nested_dir = os.path.join(base_dir, 'the newest folder')

if not os.path.exists(nested_dir):
    os.mkdir(nested_dir)
else:
    print(f"Вложенная директория {nested_dir} уже существует")


new_file_path = os.path.join(nested_dir, 'empty.txt')

if not os.path.exists(new_file_path):
    os.rename(file_path, new_file_path)
    print(f"Файл был перемещён в: {new_file_path}")
else:
    print(f"Файл уже находится в {new_file_path}")
