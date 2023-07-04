from typing_extensions import override
from battery.battery import Battery

from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery:Battery):
        self.__engine = engine
        self.__battery = battery

    @override
    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service()
