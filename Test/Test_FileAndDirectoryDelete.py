import os
import unittest
import tempfile

from FileAndDirectoryDelete import FileAndDirectoryDelete

class TestFileAndDirectoryDelete(unittest.TestCase):

    def test_FileAndDirectoryDelete(self):

        file_dir_delete = FileAndDirectoryDelete()

        self.assertIsNotNone(file_dir_delete)


