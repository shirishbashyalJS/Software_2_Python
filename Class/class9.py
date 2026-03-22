import random

class Car:
    def __init__(self, reg_num, max_speed, cur_speed=0, distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.distance = distance

    def acclerate(self, change_speed):
        self.cur_speed += change_speed
        if self.cur_speed < 0:
            self.cur_speed = 0
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed

    def drive(self, hour):
        self.distance += self.cur_speed * hour

    def get_info(self):
        return {
            "reg_num": self.reg_num,
            "max_speed": self.max_speed,
            "cur_speed": self.cur_speed,
            "distance": self.distance
        }
    
    

class Race:
    def __init__(self, name, distance_KM, cars):
        self.name = name
        self.distance_KM = distance_KM
        self.cars = cars
    
    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(10,20)
            car.drive(1)
