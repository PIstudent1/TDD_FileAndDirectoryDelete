import os
import shutil

class FileAndDirectoryDelete:

    def is_exists(self, path):
        return os.path.exists(path)


