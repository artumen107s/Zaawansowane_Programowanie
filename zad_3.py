# zad_3
from zad_1 import Student
# Stworzyć następujące klasy...

student1 = Student("Artur", [60, 70, 80])
student2 = Student("Mendela", [40, 45, 50])

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property at {self.address}, area: {self.area}, rooms: {self.rooms}, price: {self.price}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House at {self.address}, area: {self.area}, rooms: {self.rooms}, plot: {self.plot}, price: {self.price}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat at {self.address}, area: {self.area}, rooms: {self.rooms}, floor: {self.floor}, price: {self.price}"

house = House(120, 4, 300000, "123 Main St", 1000)
flat = Flat(80, 3, 200000, "456 Center Ave", 2)

house.__str__(), flat.__str__(), student1.is_passed(), student2.is_passed()

house1 = House(120, 4, 300000, "123 Main St", 1000)
flat1 = Flat(80, 3, 200000, "456 Center Ave", 2)

print(house1)
print(flat1)