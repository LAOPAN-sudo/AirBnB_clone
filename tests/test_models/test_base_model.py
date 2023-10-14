import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()
        self.base_model.name = "My First Model"
        self.base_model.my_number = 89

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_method(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'], self.base_model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
