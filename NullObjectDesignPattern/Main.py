from VehicleFactory import *

obj = VehicleFactory()
vehicle = obj.getVehicleObject("Bike")

print(vehicle.returnFuelCapacity())
print(vehicle.returnSeatingCapacity())