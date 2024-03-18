import os
import unittest
import tempfile

from FileAndDirectoryDelete import FileAndDirectoryDelete

class TestFileAndDirectoryDelete(unittest.TestCase):

    def test_FileAndDirectoryDelete(self):

        file_dir_delete = FileAndDirectoryDelete()

        self.assertIsNotNone(file_dir_delete)

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_path = self.temp_file.name
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir_path = self.temp_dir.name

    def tearDown(self):
        os.unlink(self.temp_file_path)

    def test_is_exists_file_True(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertTrue(file_dir_delete.is_exists(self.temp_file_path))

    def test_is_exists_file_False(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertFalse(file_dir_delete.is_exists(self.temp_file_path))

    def test_is_exists_dir_True(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertTrue(file_dir_delete.is_exists(self.temp_dir_path))

    def test_is_exists_dir_False(self):
        file_dir_delete = FileAndDirectoryDelete()
        self.assertFalse(file_dir_delete.is_exists(self.temp_dir_path))




