# zad_1

# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
# go wyświetlić ( print )

def printPattern(name, surname) :
    return f"Cześć {name} {surname}!"

wynik = printPattern("Artur", "Mendela")
print(wynik)