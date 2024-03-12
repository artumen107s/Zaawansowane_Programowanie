# zad_2
# Stworzyć następujące klasy...
from zad_1 import Student

student1 = Student("Artur", [60, 70, 80])
student2 = Student("Mendela", [40, 45, 50])

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}, open: {self.open_hours}, phone: {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name}, hired: {self.hire_date}, born: {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, phone: {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book by {self.author_name} {self.author_surname}, published: {self.publication_date}, {self.number_of_pages} pages, at {self.library}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ', '.join([str(book) for book in self.books])
        return f"Order by {self.student.name} handled by {self.employee.first_name} on {self.order_date}, books: {books_str}"
    
library1 = Library("Bombastic", "StreetA", "12345", "9-5", "123-456-789")
employee1 = Employee("Janek", "Stachurski", "2022-01-01", "1990-01-01", "CityA", "StreetA", "12345", "987-654-321")
book1 = Book(library1, "2022-01-01", "Tomasz", "Cichy", 300)
order1 = Order(employee1, student1, [book1], "2023-01-01")

print(library1)
print(employee1)
print(book1)
print(order1)