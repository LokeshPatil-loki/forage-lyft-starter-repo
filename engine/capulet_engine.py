from typing_extensions import override
from .engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.__current_mileage:int = current_mileage
        self.__last_service_mileage:int = last_service_mileage

    @override
    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage > 30000
