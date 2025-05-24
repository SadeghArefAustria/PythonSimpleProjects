class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, increment=5):
        self.speed += increment
        print(f"{self.make} {self.model} accelerated to {self.speed} km/h.")

    def brake(self, decrement=5):
        self.speed = max(0, self.speed - decrement)
        print(f"{self.make} {self.model} slowed down to {self.speed} km/h.")

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}, Speed: {self.speed} km/h")


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.make} {car.model} to the garage.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.make} {car.model} from the garage.")
        else:
            print("Car not found in the garage.")

    def list_cars(self):
        if not self.cars:
            print("Garage is empty.")
        else:
            print("Cars in the garage:")
            for car in self.cars:
                car.display_info()


# Example usage:
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Mustang", 2022)

    garage = Garage()
    garage.add_car(car1)
    garage.add_car(car2)

    garage.list_cars()

    car1.accelerate()
    car2.accelerate(10)
    car1.brake(3)

    garage.remove_car(car1)
    garage.list_cars()