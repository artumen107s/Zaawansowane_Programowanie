# zadanie 2

# a) Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.

def printNames(names) :
    for i in names:
        print(i)

printNames(["Artur", "Tomasz", "Klaudia", "Krystian", "Karolina"])

# b) Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:

def modifyList(numbers) :
    for i in range(len(numbers)):
        numbers[i]*=2
    print(numbers)
    return numbers

modifyList([12, 17, 63, 82, 2])

def modifyListTwo(numbers) : 
    return [x * 2 for x in numbers]

modifyListTwo([12, 17, 63, 82, 2])

# c) Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# jedynie parzyste elementy.

def printEven(numbers):
    for i in range(len(numbers)):
        if (numbers[i]%2 == 0):
            print(numbers[i])

printEven([12, 17, 63, 82, 2, 7, 2, 1, 8, 7])

# d) Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

def printSecond(numbers):
    for i in range(len(numbers)):
        if (i%2 == 0):
            print(numbers[i])

printSecond([12, 17, 63, 82, 2, 7, 2, 1, 8, 7])
