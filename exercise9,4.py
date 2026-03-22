# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of
#  the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of 
# each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows:
#  "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are
#  performed:

# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
#  This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of 
# each car are printed out formatted into a clear table.

from Class.class9 import Car
from tabulate import tabulate 
import random

cars = []

for i in range(10):
    reg_num = "ABC-" + str(i+1)
    max_speed = random.randint(100, 200)
    car= Car(reg_num, max_speed)
    cars.append(car)

race = True
while race:
    for car in cars:
        car.acclerate(random.randint(-15,10))
        car.drive(1)
        if car.distance >= 10000:
            race = False

printable_cars = []
for car in cars:
    printable_cars.append(car.get_info())
table = tabulate(printable_cars, headers="keys", tablefmt="fancy_grid")
print(table)
