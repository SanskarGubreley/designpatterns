from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def returnSeatingCapacity(self):
        pass
    
    @abstractmethod
    def returnFuelCapacity(self):
        pass