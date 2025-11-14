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

# both lists and tuples can be used in real life projects like storing a collection of items, representing a record or a data structure, etc.

# for example using a tuple to represent a student record
student_record = ("Jake", 25, "Emobilis")
print(student_record)

# another example for list
shopping_list = ["Milk", "Bread", "Eggs"]
print(shopping_list)


# sets are unordered collections of unique items defined using curly braces {} or the set() function. they do not allow duplicate values and do not maintain any specific order of elements.
colors = {"Red", "Green", "Blue", "Red"}  # Red is duplicated
print(colors)  # Output will be {'Red', 'Green', 'Blue'} without duplicates

# adding an item to a set
colors.add("Yellow")    
print(colors)

# removing an item from a set 
colors.remove("Green")
print(colors) 

# in real life sets can be used for storing unique items like tags, categories, etc.
# for example storing unique tags for a blog post
blog_tags = {"Python", "Programming", "Tutorial", "Python"}  # Python is duplicated
print(blog_tags)  # Output will be {'Python', 'Programming', 'Tutorial'} without duplicates 

# time complexity
# lists have O(n) time complexity for search operations because they are ordered collections and may require traversing the entire list to find an item.
# tuples also have O(n) time complexity for search operations for the same reason as lists. 
# sets have O(1) average time complexity for search operations because they use hash tables for storing items, allowing for faster lookups. 
# therefore, sets are generally more efficient for membership testing compared to lists and tuples.
# for example, checking if an item exists in a set is faster than checking in a list or tuple.
print("Red" in colors)  # True
print("Purple" in colors)  # False  
print("Banana" in fruits)  # False
print("Jake" in student_record)  # True 
# overall, the choice between lists, tuples, and sets depends on the specific use case and requirements of the application. 
# lists are suitable for ordered collections that may require modifications, tuples are ideal for fixed collections of items that should not change, and sets are best for storing unique items with efficient membership testing.


# dictionaries are collections of key-value pairs defined using curly braces {} with keys and values separated by colons. they allow for fast lookups, insertions, and deletions based on keys.
student = {
    "name": "Jake",
    "age": 25,
    "course": "Emobilis"
}
print("student name is", student["name"])
# accessing values using keys
print(student["name"])  # Jake

# adding a new key-value pair
student["grade"] = "A"
print("student grade is", student["grade"])
# updating an existing value
student["age"] = 26
print("student age is", student["age"])

# removing a key-value pair
del student["course"]
print(student)  

# in real life dictionaries can be used for storing structured data like records, configurations, etc.
# for example storing a product record

product = {
    "id": 101,  
    "name": "Laptop",
    "price": 1500.00,
    "in_stock": True  
}
print(product["name"])  

# time complexity
# dictionaries have O(1) average time complexity for search, insertion, and deletion operations because they use hash tables for storing key-value pairs, allowing for fast lookups based on keys.
# therefore, dictionaries are generally more efficient for operations that involve accessing data based on keys compared to
# lists and tuples. 
# for example, checking if a key exists in a dictionary is faster than checking in a list or tuple.
print("name" in student)  # True  
print("course" in student)  # False
print("id" in product)  # True
print("price" in product)  # True
# overall, dictionaries are ideal for storing structured data that requires fast access based on keys, making them suitable for various applications such as databases, configurations, and records.

# end of ds.py

# today we have covered lists, tuples, sets, and dictionaries in Python. we have discussed their definitions, characteristics, real-life applications, and time complexities for various operations. understanding these data structures is crucial for efficient programming and data management in Python.
# end of datatype.py# datatype.py
