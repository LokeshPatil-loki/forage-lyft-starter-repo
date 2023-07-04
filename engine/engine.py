from abc import ABC, abstractmethod

class Engine(ABC):
    def needs_service() -> bool:
        pass