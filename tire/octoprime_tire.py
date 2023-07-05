from typing_extensions import override
from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self,tire_wear_array:list[float]) -> None:
        self.__tire_wear_array = tire_wear_array
    
    @override
    def needs_service(self) -> bool:
        return sum(self.__tire_wear_array) >= 3
