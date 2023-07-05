from datetime import date
import unittest
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from utils import add_years_to_date


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesent_need_service(self):
        current_mileage = 60000
        last_service_mileage = 50000
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_doesent_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 130000
        last_service_mileage = 60000
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesent_need_service(self):
        current_mileage = 60000
        last_service_mileage = 50000
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.today()
        last_service_date = add_years_to_date(current_date,-4)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_doesent_need_service(self):
        current_date = date.today()
        last_service_date = add_years_to_date(current_date,-1)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.today()
        last_service_date = add_years_to_date(current_date,-3)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_doesent_need_service(self):
        current_date = date.today()
        last_service_date = add_years_to_date(current_date,-1)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())

unittest.main()