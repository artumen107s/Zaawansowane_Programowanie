# zad_3

# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def checkEven(a):
    return (a%2 == 0)

wynik = checkEven(4)

if (wynik == True) :
    print("Liczba parzysta")
else: print("Liczba nieparzysta")