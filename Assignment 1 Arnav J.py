
# Assignment 1 :Write a python program to create a Dictionary, Tuple and List of students 
# and perform the following operations on the dictionary: Add, Delete, Update.


# Create a list
student_list = ["John", "May", "Micheal"]
print(student_list)


# Create a tuple
fruits = ("apple", "banana", "mango")
print(fruits)



# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "college": "MIT-WPU"
}

# Add
student["city"] = "Mumbai"
print("\nAfter Adding:", student)

# Update
student["age"] = 21
print("\nAfter Updating:", student)

# Delete
del student["college"]
print("\nAfter Deleting:", student)