# Extend the program again by adding a method fire_alarm that
#  does not receive any parameters and moves all elevators to
#  the bottom floor. Continue the main program by causing a 
# fire alarm in your building.

from Class.class10 import Elevator, Building

tripla = Building(5, 5, 5)

tripla.run_elevator(1,2)
tripla.run_elevator(2,5)
tripla.run_elevator(3,5)
tripla.run_elevator(4,2)
tripla.run_elevator(5,1)

tripla.fire_alarm()