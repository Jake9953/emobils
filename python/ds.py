# list ds.py
mayina = ["Jacobs", "Wambua", "Emobilis", "Class"]
print(mayina)

print(mayina[0])  # Jacobs

# list are mutable
mayina[0] = "Jake"
print(mayina)
print(mayina[0])  # Jake



# tuples are immutable and cannot be changed and are defined using parentheses and not square brackets so use () instead of [] to define a tuple you cannot change the values of a tuple once it is created but you can access the values using indexing like lists but you cannot change the values of a tuple once it is created. so to access the values of a tuple you can use indexing like lists but you cannot change the values of a tuple once it is created.

fruits = ("Mango", "Banana", "Orange")
print(fruits)

# accessing tuple values using indexing
print(fruits[1])  # Banana

# trying to change the value of a tuple will result in an error
# fruits[1] = "Pineapple"  # This will raise a TypeError?