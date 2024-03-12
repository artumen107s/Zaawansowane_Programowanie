# zad_5

# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def check(a,b):
    return b in a

wynik = check([5,4,3,2,1], 2)
print(wynik)