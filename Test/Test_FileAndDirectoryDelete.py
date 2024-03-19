import os
import unittest
import tempfile

from FileAndDirectoryDelete import FileAndDirectoryDelete

class TestFileAndDirectoryDelete(unittest.TestCase):

    def test_FileAndDirectoryDelete(self):

        file_dir_delete = FileAndDirectoryDelete()

        self.assertIsNotNone(file_dir_delete)

    def test_is_exists_file_True(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        file_dir_delete = FileAndDirectoryDelete()
        self.assertTrue(file_dir_delete.is_exists(temp_file_path))
        temp_file.close()
        os.unlink(temp_file_path)

    def test_is_exists_file_False(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertFalse(file_dir_delete.is_exists("/non/existent/path"))

    def test_is_exists_dir_True(self):
        temp_dir = tempfile.TemporaryDirectory()
        temp_dir_path = temp_dir.name
        file_dir_delete = FileAndDirectoryDelete()
        self.assertTrue(file_dir_delete.is_exists(temp_dir_path))
        temp_dir.cleanup()

    def test_is_exists_dir_False(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertFalse(file_dir_delete.is_exists("/non/existent/path"))

    def test_destroy_file(self):
        file_dir_delete = FileAndDirectoryDelete()
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        with open(temp_file.name, 'w') as f:
            f.write('test data')
        temp_file.close()
        file_dir_delete.destroy_file(temp_file.name)
        self.assertFalse(os.path.exists(temp_file.name))

    def test_destroy_directory(self):
        file_dir_delete = FileAndDirectoryDelete()
        test_dir = tempfile.mkdtemp()
        test_file = os.path.join(test_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write('test data')
        file_dir_delete.destroy_directory(test_dir)
        self.assertFalse(os.path.exists(test_dir))

    def test_check_access_file(self):
        file_dir_delete = FileAndDirectoryDelete()
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.close()
        self.assertTrue(file_dir_delete.check_access(temp_file.name))
        os.unlink(temp_file.name)


    def test_check_access_directory(self):
        file_dir_delete = FileAndDirectoryDelete()
        temp_dir = tempfile.TemporaryDirectory()
        self.assertTrue(file_dir_delete.check_access(temp_dir.name))
        temp_dir.cleanup()





