# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars
#  have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the
#  tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric
#  cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the
#  initializer of the base class to set the first two properties and then sets its capacity. Write a main 
# program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h,
#  32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer
#  counters.

from Class.class9 import *


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.acclerate(120)
gasoline_car.acclerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car's KM counter: {electric_car.distance} KM")
print(f"Gasoline car's KM counter: {gasoline_car.distance} KM")


