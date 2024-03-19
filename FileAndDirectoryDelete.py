import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileAndDirectoryDelete:
    def __init__(self, root, overwrite_times=10, overwrite_char='0'):
        self.root = root
        self.root.geometry("800x600")
        self.file_path = tk.StringVar()
        self.dir_path = tk.StringVar()
        self.choosen = tk.StringVar(value='None')
        self.overwrite_times = overwrite_times
        self.overwrite_char = overwrite_char
        self.create_widgets()

    def is_exists(self, path):
        return os.path.exists(path)

    def check_access(self, path):
        return os.access(path, os.W_OK)

    def destroy_file(self, file_path):
        if not self.is_exists(file_path):
            messagebox.showerror("Ошибка", f"Файл {file_path} не найден.")
            return

        if not self.check_access(file_path):
            messagebox.showerror("Ошибка", f"Нет доступа к файлу {file_path}.")
            return

        with open(file_path, "r+") as file:
            length = os.path.getsize(file_path)
            for _ in range(self.overwrite_times):
                file.seek(0)
                file.write(self.overwrite_char * length)
        os.remove(file_path)
        messagebox.showinfo("Результат", f"Файл {file_path} успешно уничтожен.")



    def destroy_directory(self, dir_path):
        if not self.is_exists(dir_path):
            messagebox.showerror("Ошибка", f"Папка {dir_path} не найдена.")
            return

        if not self.check_access(dir_path):
            messagebox.showerror("Ошибка", f"Нет доступа к папке {dir_path}.")
            return

        for root, dirs, files in os.walk(dir_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                self.destroy_file(file_path)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(dir_path)
        messagebox.showinfo("Результат", f"Папка {dir_path} успешно уничтожена.")


    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
        return file_path

    def select_directory(self):
        directory_path = filedialog.askdirectory()
        self.file_path.set(directory_path)
        return directory_path

    def delete_selection(self):
        selection = self.choosen.get()
        if selection == 'File':
            self.label_1.config(text='Файл для уничтожения:')
            self.select_file()
        if selection == 'Dir':
            self.label_1.config(text='Папка для уничтожения:')
            self.select_directory()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Выберете, что уничтожить:")
        self.label.pack()
        self.radio_file = tk.Radiobutton(self.root, variable=self.choosen, text='Файл', value='File', command=self.delete_selection)
        self.radio_file.pack()
        self.radio_dir = tk.Radiobutton(self.root, variable=self.choosen, text='Папка', value='Dir', command=self.delete_selection)
        self.radio_dir.pack()

        self.label_1 = tk.Label(self.root, text="Файл для уничтожения:")
        self.label_1.pack()

        self.entry = tk.Entry(self.root, textvariable=self.file_path, width=100)
        self.entry.pack()

        self.destroy_button = tk.Button(self.root, text="Удалить", command=self.destroy)
        self.destroy_button.pack()


    def destroy(self):
        path = self.file_path.get()
        selection = self.choosen.get()
        if selection == 'File':
            if not messagebox.askyesno("Подтверждение", f"Выбранный файл будет бесследно удален! Вы уверены, что хотите удалить файл {path}?"):
                return
            self.destroy_file(path)

        if selection == 'Dir':
            if not messagebox.askyesno("Подтверждение", f"Выбранная папка и все файлы в ней будут бесследно удалены! Вы уверены, что хотите удалить папку {path}?"):
                return
            self.destroy_directory(path)










