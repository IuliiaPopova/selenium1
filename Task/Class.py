class Car(object):
    """Class creates car"""
    odometer = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description_name(self):
        desc = str(self.year) + " " + self.make + " " + self.model
        return desc.title()

    def read_odometer(self):
        print("Odometer shows " + str(self.odometer))

    def update_odom(self, km):
        if km >= self.odometer:
            self.odometer = km
        else:
            print("Stop")

    def increment_odom(self, km):
        self.odometer += km
        return self.odometer


class Battery():
    def __init__(self,battery=100):
        self.battery=battery
    def desc_battery(self):
        print("This car has the powell: " +str(self.battery))


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


ElectricCar("tesla","s",2017).battery.desc_battery()
