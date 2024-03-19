import keyboard
import tkinter as tk

from FileAndDirectoryDelete import FileAndDirectoryDelete

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Бесследный уничтожитель файлов и папок')
    file_dir_delete = FileAndDirectoryDelete(root)
    root.mainloop()




