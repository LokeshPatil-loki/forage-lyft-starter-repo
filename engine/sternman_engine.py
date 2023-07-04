from typing_extensions import override

from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.__warning_light_is_on:bool = warning_light_is_on

    @override
    def needs_service(self):
        if self.__warning_light_is_on:
            return True
        else:
            return False
