import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_default_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_custom_attributes(self):
        amenity = Amenity()
        amenity.name = "Banes"
        self.assertEqual(amenity.name, "Banes")

    def test_str_representation(self):
        amenity = Amenity()
        amenity.name = "Banes"
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_id_generation(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_id_is_string(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)


if __name__ == '__main__':
    unittest.main()
