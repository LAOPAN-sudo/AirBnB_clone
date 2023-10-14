import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        # Add more attribute-specific tests here.

    def test_city_str_representation(self):
        city = City()
        city.name = "Los Angeles"
        city.state_id = "CA"
        expected_str = "[City] ({}) {}".format(city.id,city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_city_to_dict(self):
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        city_dict = city.to_dict()
        self.assertEqual(city_dict['id'], "{}".format(city.id))
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['__class__'], "City")
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_city_update_attributes(self):
        city = City()
        city.name = "City Name"
        city.state_id = "State ID"
        
        new_name = "New City Name"
        new_state_id = "New State ID"
        
        city.name = new_name
        city.state_id = new_state_id
        
        self.assertEqual(city.name, new_name)
        self.assertEqual(city.state_id, new_state_id)
"""
    def test_city_create_new_instance(self):
        city = City()
        city.name = "New City"
        city.state_id = "New State"
        city.save()
        
        all_cities = City.all()
        self.assertTrue(city in all_cities)
"""
    def test_city_delete_instance(self):
        city = City()
        city.name = "City to delete"
        city.state_id = "State to delete"
        city.save()

        city_id = city.id
        city.delete()

        all_cities = City.all()
        self.assertTrue(city_id not in [city.id for city in all_cities])


if __name__ == '__main__':
    unittest.main()

