from Car import *
from NullVehicle import *

class VehicleFactory:

    def getVehicleObject(self,carType):
        if carType == "car":
            return Car()
        else:
            return NullVehicle()