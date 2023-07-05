from datetime import date
from typing_extensions import override

from utils import add_years_to_date
from .battery import Battery

class NubbinBattery(Battery):
    def __init__(self,last_service_date: date,current_date:date):
        self.__last_service_date:date = last_service_date
        self.__current_date:date = current_date
    
    @override
    def needs_service(self) -> bool:
        date_which_battery_should_be_serviced_by = add_years_to_date(self.__last_service_date,4)
        return date_which_battery_should_be_serviced_by <= self.__current_date