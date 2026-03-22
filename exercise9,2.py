# Extend the program by adding an accelerate method into the new class. The method should
#  receive the change of speed (km/h) as a parameter. If the change is negative, the car
#  reduces speed. The method must change the value of the speed property of the object.
#  The speed of the car must stay below the set maximum and cannot be less than zero.
#  Extend the main program so that the speed of the car is first increased by +30 km/h,
#  then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
#  Finally, use the emergency brake by forcing a -200 km/h change on the speed and then
#  print out the final speed. The travelled distance does not have to be updated yet.

from Class.class9 import Car

car = Car("AB-X", 500)

car.acclerate(30)
car.acclerate(70)
car.acclerate(50)
print(f"The Current speed of the Car is {car.cur_speed} km/hr")
car.acclerate(-200)
print(f"The Current speed of the Car is {car.cur_speed} km/hr")


