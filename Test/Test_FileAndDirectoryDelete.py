import os
import unittest
import tempfile

class TestFileAndDirectoryDelete(unittest.TestCase):

    def FileAndDirectoryDeleteTest(self):

        file_dir_delete = FileAndDirectoryDelete()

        self.assertIsNotNone(file_dir_delete)