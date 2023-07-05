import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear_array = [0,0.9,0.6,1]
        tire = CarriganTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_need_service_false(self):
        tire_wear_array = [0,0.24,0.6,0.89]
        tire = CarriganTire(tire_wear_array)
        self.assertFalse(tire.needs_service())