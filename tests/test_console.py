from models import storage
from models.base_model import BaseModel
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestCreateCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_string_param(self, mock_stdout):
        """Test create command with string parameter"""
        cmd = HBNBCommand()
        cmd.onecmd("create BaseModel name=\"My_little_house\"")

        # Retrieve the ID of the created object from the console output
        created_id = mock_stdout.getvalue().strip()

        # Retrieve the created object from the storage
        created_obj = storage.all()["BaseModel.{}".format(created_id)]

        # Check if the name attribute of the created object matches the
        # expected value
        self.assertEqual(created_obj.name, "My little house")
        # self.assertIn("My little house", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_float_param(self, mock_stdout):
        """Test create command with float parameter"""
        cmd = HBNBCommand()
        cmd.onecmd("create BaseModel price=10.5")

        # Retrieve the ID of the created object from the console output
        created_id = mock_stdout.getvalue().strip()

        # Retrieve the created object from the storage
        created_obj = storage.all()["BaseModel.{}".format(created_id)]

        # Check if the price attribute of the created object matches the
        # expected value
        self.assertEqual(created_obj.price, 10.5)

    # Add more test methods for other parameter types as needed...


if __name__ == '__main__':
    unittest.main()
