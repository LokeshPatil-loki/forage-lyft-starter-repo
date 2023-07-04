from typing_extensions import override
from .engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    @override
    def needs_service(self):
        return self.__current_mileage - self.__last_service_mileage > 60000
