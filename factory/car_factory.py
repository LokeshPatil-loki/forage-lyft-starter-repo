from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @classmethod
    def create_calliope(cls,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery)
    
    @classmethod
    def create_glissade(cls,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery)
    
    @classmethod
    def create_palindrome(cls,current_date: date, last_service_date: date,warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery)
    
    @classmethod
    def create_rorschach(cls,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        return Car(engine,battery)
    
    @classmethod
    def create_thovex(cls,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        return Car(engine,battery)