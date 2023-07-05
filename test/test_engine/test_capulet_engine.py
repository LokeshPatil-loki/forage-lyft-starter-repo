import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 50000
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())