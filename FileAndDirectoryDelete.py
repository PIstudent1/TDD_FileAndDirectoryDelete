import os
import shutil

class FileAndDirectoryDelete:
    def __init__(self, overwrite_times=10, overwrite_char='0'):
        self.overwrite_times = overwrite_times
        self.overwrite_char = overwrite_char

    def is_exists(self, path):
        return os.path.exists(path)

    def check_access(self, path):
        return os.access(path, os.W_OK)

    def destroy_file(self, file_path):
        if not self.is_exists(file_path):
            print(f"Файл {file_path} не найден.")
            return

        with open(file_path, "r+") as file:
            length = os.path.getsize(file_path)
            for _ in range(self.overwrite_times):
                file.seek(0)
                file.write(self.overwrite_char * length)
        os.remove(file_path)
        print(f"Файл {file_path} успешно уничтожен.")



    def destroy_directory(self, dir_path):
        if not self.is_exists(dir_path):
            print(f"Папка {dir_path} не найдена.")
            return

        for root, dirs, files in os.walk(dir_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                self.destroy_file(file_path)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(dir_path)
        print(f"Папка {dir_path} успешно уничтожена.")






