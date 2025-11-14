class Students:
  # Constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # Method to display student information
  def display_info(self):
    print(f"Name: {self.name}, Age: {self.age}")

    # method to check if the student is an adult
  def is_adult(self):
    if self.age >= 18:
      print(f"{self.name} is an adult.")
    else:
      print(f"{self.name} is not an adult.")

      # create objects of the Students class
student1 = Students("Alice", 20)
print("is student1 an adult?")
student1.is_adult()
student2 = Students("Bob", 16)
print("is student2 an adult?")
student2.is_adult()

# So the above starting line 1, is a comment that explains the purpose of the code.
# The code defines a class `Students` with methods to display student information and check if the student is an adult.
# Two objects of the class are created which are `student1` and `student2`.
# The code then checks if each student is an adult and prints the result. 
# The output will indicate whether each student is an adult based on their age.
# The code demonstrates basic object-oriented programming concepts in Python.

# we could another example to understand the concept of OOP in Python.
class Car:
    # Constructor that initializes the car's make, model, and year
    # when creating a constructor, we use the __init__ method, that is a special method in Python classes.
    # It is called when an object of the class is instantiated.
    # the def, keyword is used to define a method in Python.
    # the init method takes the parameters self, make, model, and year.
    # The self parameter refers to the instance of the class itself. meaning that it allows us to access the attributes and methods of the class in Python.
    # The make, model, and year parameters are used to initialize the attributes of the car
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year

    # Method to display car information. we use the display_info method to print the car's make, model, and year.
    # This method uses an f-string to format the output.
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

    # Method to check if the car is vintage, is not a must or its must to have this method in the class.
    # This method checks if the car is older than 25 years from the current year (2023).
    # It compares the current year (2023) with the car's year and prints whether the car is vintage or not.
    # The method uses an if statement to check the condition and prints the appropriate message. so we can use this method to check if the car is vintage or not.
    # The method does not return any value, it just prints the result.
    def is_vintage(self):
        # This method checks if the car is older than 25 years from the current year (2023).
        if 2023 - self.year > 25:
            print(f"{self.make} {self.model} is a vintage car.")
        else:
            print(f"{self.make} {self.model} is not a vintage car.")

# Create objects of the Car class
car1 = Car("Toyota", "Camry", 1995) 
print("Car 1 Information:")
car1.display_info()  # Display information for car1
car1.is_vintage()  # Check if car1 is vintage

car2 = Car("Tesla", "Model S", 2018)
print("\nCar 2 Information:") 
car2.display_info()  # Display information for car2
car2.is_vintage()  # Check if car2 is vintage

# The above code defines a class `Car` with methods to display car information and check if the car is vintage.
# Two objects of the class are created, `car1` and `car2`.
# The code then displays the information for each car and checks if each car is vintage based on its year.
# This code demonstrates basic object-oriented programming concepts in Python, including class definition, constructor, methods, and object instantiation.
# The output will indicate the make, model, year of each car and whether it is vintage or not.


# another exapmple to understand the concept of OOP in Python. using how mpesa works to deposit and check balance.
class Mpesa:
    # Constructor to initialize the Mpesa account with a balance
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0  # Initial balance is set to 0.0

    # Method to deposit money into the Mpesa account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Ksh {amount}. New balance: Ksh {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to check the current balance of the Mpesa account
    def check_balance(self):
        print(f"Current balance for account {self.account_number}: Ksh {self.balance}")
    # Method to simulate sending money to another Mpesa account
    def send_money(self, recipient_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Sent Ksh {amount} to account {recipient_account}. New balance: Ksh {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
    # Method to simulate receiving money from another Mpesa account
    def receive_money(self, sender_account, amount):
        if amount > 0:
            self.balance += amount
            print(f"Received Ksh {amount} from account {sender_account}. New balance: Ksh {self.balance}")
        else:
            print("Received amount must be positive.")
# Create an instance of the Mpesa class
mpesa_account = Mpesa("254712345678") 
# Deposit money into the Mpesa account
mpesa_account.deposit(1000)  # Deposit Ksh 1000
# Check the current balance   
mpesa_account.check_balance()  # Check balance after deposit
# Send money to another Mpesa account
mpesa_account.send_money("254723456789", 500)  # Send Ksh 500
# Check the balance after sending money 
mpesa_account.check_balance()  # Check balance after sending money
# withdraw money from the Mpesa account
mpesa_account.send_money("254734567890", 200)  # Send Ksh 200
# Check the balance after sending money
mpesa_account.check_balance()  # Check balance after sending money

# basically, OOP in Python allows us to create classes that encapsulate data and behavior related to that data.
# In this example, we created a `Mpesa` class that represents an Mpesa account  
# with methods to deposit money, check balance, send money, and receive money.
# We then created an instance of the `Mpesa` class and performed various operations on it
# to demonstrate how OOP works in Python.
# This code demonstrates the principles of object-oriented programming (OOP) in Python.
# OOP allows us to model real-world entities and their interactions in a structured way.
# The code defines a class `Mpesa` with methods to deposit money, check balance, send money, and receive money.
# An instance of the `Mpesa` class is created, and various operations are performed to demonstrate how OOP works in Python.

# In summary, the code demonstrates how to create classes, define methods, and interact with objects in Python.
# This is a fundamental concept in OOP, allowing us to organize code and model real-world entities effectively.

# to practice oop, tackle the following exercises:

# 1. Create a class `Book` with attributes like title, author, and publication year.
#    Implement methods to display book information and check if the book is a classic (published more than 50 years ago). 
# 

class Book:
  # constructor
  def __init__(self, title, author, publication):
    self.title = title
    self.author = author
    self.publication = publication

    # method to display
  def display_info(self):
    print(f"The book {self.title} is writen by {self.author} and was published in the year {self.publication}")
    
  def is_classic(self):
       if 2025 - self.publication > 50:
          print(f"The Book{self.title} writen by {self.author} is a classis")
       else:
          print(f"The Book {self.title} writen by {self.author} is not a classic")

# objects
book1 = Book("5AM Club", "Robin Sharma", 2055)
print("Book1 information:")
book1.display_info()
book1.is_classic()

    


# 2. Create a class `BankAccount` with methods to deposit, withdraw, and check balance.
#    Implement error handling for insufficient funds during withdrawal. 
# 3. Create a class `Library` that manages a collection of books.
#    Implement methods to add a book, remove a book, and display all books in the library.
# 4. Create a class `Person` with attributes like name, age, and occupation.
#    Implement methods to display personal information and check if the person is eligible for retirement (age >= 60).
# 5. Create a class `Movie` with attributes like title, director, and release year.
#    Implement methods to display movie information and check if the movie is a classic (released more than 20 years ago).

# These exercises will help you practice OOP concepts such as class definition, attributes, methods, and object instantiation in Python.