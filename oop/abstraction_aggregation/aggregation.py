class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # aggregation

    def show_info(self):
        print("Car Model:", self.model)
        print("Engine Horsepower:", self.engine.horsepower)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

engine1 = Engine(200)

car1 = Car("Toyota", engine1)

car1.show_info()
