# There are three different types of data in python
# name:
# String
# Number
# Boolean
# tuples type of data structure, a containers, used to store different values

character_name = input("enter your name: ")
character_age = input("enter age: ")

print("there once was a man named " + character_name + ",")
print("he was " + str(character_age) + " years old.")
print("he really loved the name " + character_name)
print("but couldn't wait to achieve his dreams at " + str(character_age) + " years")


def say_hi(name, age):
    print(name + " is the GOAT at " + age)


say_hi(character_name, character_age)


def cube(num):
    return num * num * num


result = cube(5)
print(result)
