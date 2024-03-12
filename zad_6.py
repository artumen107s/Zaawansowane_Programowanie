# zad_6

# 6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def modifyList(a,b):
   combined_list = a + b
   unique_list = []
   for item in combined_list:
      if item not in unique_list:
         unique_list.append(item)

   for i in range(len(unique_list)):
       unique_list[i] **=3
   return unique_list

print(modifyList([1,2,3], [4,5,6]))