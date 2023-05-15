class Car:
    def __init__(self):
        self.__petrol = 0
        self.__mpp = 0
        self.__odometer = 0
    
    def fill_up(self):
        if self.__petrol < 60:
            self.__petrol = 60

    def drive(self, km):
        gas_needed = km
        if gas_needed > self.__petrol:
            driven = self.__petrol
            self.__odometer += driven
            self.__petrol = 0
            return f"Car ran out of petrol after driving {driven} km"
        else:
            self.__odometer += km
            self.__petrol -= gas_needed
            return f"Car Drove {km} km"

    
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"



if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
