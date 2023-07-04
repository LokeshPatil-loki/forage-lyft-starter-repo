from datetime import date
from typing_extensions import override
from .battery import Battery

class NubbinBattery(Battery):
    def __init__(self,last_service_date: date,current_date:date):
        self.__last_service_date = last_service_date
        self.__current_date = date.today()
    
    @override
    def needs_service(self) -> bool:
        self.__current_date = date.today()
        years = (self.__current_date - self.__last_service_date).days * 365
        return years >= 4