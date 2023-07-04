from abc import ABC, abstractmethod
from battery.battery import Battery

from engine.engine import Engine


class Car(ABC):
    def __init__(self, engine: Engine, battery:Battery):
        

    @abstractmethod
    def needs_service(self):
        pass
