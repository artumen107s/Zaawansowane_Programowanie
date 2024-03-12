# zad_1

# 1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50

student1 = Student("Artur", [60, 70, 80])
student2 = Student("Mendela", [40, 45, 50])

print(f"{student1.name} passed: {student1.is_passed()}")
print(f"{student2.name} passed: {student2.is_passed()}")