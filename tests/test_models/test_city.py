import unittest
class TestCity(unittest.TestCase):
    def test_true(self):
        """
        """
        self.assertTrue(True)
    
    def test_flase(self):
        """
        """
        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()