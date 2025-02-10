import os
import tkinter as tk
from tkinter import filedialog, messagebox
from github import Github

# Функция для загрузки файла на GitHub
def upload_file_to_github():
    # Получаем путь к файлу
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Получаем информацию о репозитории
    repo_name = repo_entry.get()
    access_token = token_entry.get()

    try:
        # Подключаемся к GitHub
        g = Github(access_token)
        repo = g.get_repo(repo_name)

        # Получаем имя файла
        file_name = os.path.basename(file_path)

        # Загружаем файл в репозиторий
        with open(file_path, "rb") as file:
            content = file.read()
            repo.create _file(file_name, content, "Upload file via app")

        messagebox.showinfo("Success", f"File '{file_name}' uploaded successfully to '{repo_name}'!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Создаем основное окно приложения
root = tk.Tk()
root.title("GitHub File Uploader")

# Поле для ввода имени репозитория
repo_label = tk.Label(root, text="Repository (username/repo):")
repo_label.pack()
repo_entry = tk.Entry(root, width=50)
repo_entry.pack()

# Поле для ввода токена доступа
token_label = tk.Label(root, text="Access Token:")
token_label.pack()
token_entry = tk.Entry(root, width=50, show='*')
token_entry.pack()

# Кнопка для загрузки файла
upload_button = tk.Button(root, text="Upload File", command=upload_file_to_github)
upload_button.pack()

# Запуск основного цикла приложения
root.mainloop()