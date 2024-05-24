class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


car = Car("Toyota", "Corolla", 2022)


print("Accelerating:")
for _ in range(5):
    car.accelerate()
    print(car.get_speed())


print("Braking:")
for _ in range(5):
    car.brake()
    print(car.get_speed())




class Buffer:
    def __init__(self):
        self.current_part = []

    def add(self, *a):
        self.current_part.extend(a)
        while len(self.current_part) >= 5:
            print(sum(self.current_part[:5]))
            self.current_part = self.current_part[5:]

    def get_current_part(self):
        return self.current_part


buffer = Buffer()
buffer.add(1, 2, 3)
buffer.add(4, 5, 6, 7, 8, 9)
print("Current part:", buffer.get_current_part())
buffer.add(10, 11)
print("Current part:", buffer.get_current_part())
