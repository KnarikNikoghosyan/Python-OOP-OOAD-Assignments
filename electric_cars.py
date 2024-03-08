class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.vehicle_count = self.vehicle_count



    @classmethod
    def increment_vehicle_count(cls):
        cls.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    def start_engine(self):
        print("Engine Started")


class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels=4):
        super().__init__(make, model)
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f'This car is made in: {self.make}\nModel of car: {self.model}\nNumber of wheels: {self.number_of_wheels}'

    def start_engine(self):
        print("Car Engine Started")
        super().start_engine()


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

class ElectricCar(Car, ElectricVehicle):
   def __init__(self, make, model, battery_capacity):
       Car.__init__(self, make, model)
       ElectricVehicle.__init__(self, make, model, battery_capacity)

       def start_engine(self):
                print("Electric Car Engine started")
                super().start_engine()


car = Car(2020, "Tesla", 4)
print(car)

print(car.get_vehicle_count())
