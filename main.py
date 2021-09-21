# print("Hello World")
# age = 20        #int
# price = 19.95   #double
# first_name = 'Mosh'  # string
# is_online = False    # bool, case sensitive
# print(age)           # print variable
# # print and input are general purpose functions
# # they don't belong to objects
#
# # Exercise:
# # check in patient names John Smith
# # he is 20 years old
# # he is a new patient
# patient_name = 'John Smith'
# age = 20
# is_new = True
#
# # Type casting input variables and printing
# name = input("What is your name? ") # assign input to variable
# print("Hello " + name) # string concatenation
#
# # convert values from one to another
# birth_year = input("Enter your birth year: ")
# # age = 2020 - birth_year ERROR types mismatch
# age = 2020 - int(birth_year) # type conversion casting
# print(age)
# # converting
# # int()
# # float()
# # bool()
# # str()
#
# # Exercise
# # Basic Calculator, Print the sum of two input numbers
# first = input("First: ")
# # we can also do float(input("First: "))
# second = input("Second: ")
# # type cast the two inputs
# answer = float(first) + float(second)
# print("Sum: " + str(answer))
#
# # string stuff
# course = 'Python for Beginners'
# # method upper is part of an object str
# print(course.upper())
# # PYTHON FOR BEGINNERS
# print(course.lower())
# # python for beginners
# print(course.find('y'))
# # finds array index start at 0, -1 if unbound
# print(course.find('for'))
# # returns where the word starts in index:7
# print(course.replace('for', '4'))
# # replace the parts of string with second parameter
# # Python 4 Beginners
# # Nothing happens if not found is being replaced
# # replace generates new string, strings are immutable
# # True or false finding
# print('Python' in course)
#
# # arithmetic operators + - * / and  // % **(exponent)
# # /: floating point //:integer
# # augmented assignment operator
# x = 10
# # x = x + 3
# x += 3
# # operator precedence use parenthesis
# # comparable values < > <= >= == !=
# x = 3 == 2
# print(x)
#
# # logical operator
# price = 25
# print(price > 10 and price < 30)
# price = 5
# print(price > 10 or price < 30)
# # inverse
# print(not price > 10)
#
#
# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20: # (20, 35]
#     print("It's a nice day")
# elif temperature > 10: # (10, 20]
#     print("It's a bit cold")
# else:                   # if none apply
#     print("It's cold")
# # shift and tab to get out of block of code
# # uses indentation to represent {}
# print("Done")
#

# # input weight, convert to kg or lbs using upper/lower K L
# weight = float(input("Weight: "))
# selection = input("(K)g or (L)bs: ")
# if selection.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kg: " + str(converted))
#
# # While loops
# # print 1 - 5
# i = 1
# while i <= 1_000:
#     print(i)
#     i = i + 1
# # value of i changed to 1001
# # print(i)
# # you can multiple num by string, prints as many times
# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# # Lists, list of num or objects
# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# print(names[0])
# # prints john first element
# print(names[-2])
# # second element from end
# names[0] = "Jon"
# # can replace the element
# print(names[0:3])
# # prints first 3 names in list - doesn't change original
# print(names)
#

# # List Methods
# numbers = [1, 2, 3, 4, 5]
# # append add a number at the end
# numbers.append(6)
# print(numbers)
# # insert in start or end of list
# numbers.insert(0, -1)
# print(numbers)
# # remove
# numbers.remove(3)
# print(numbers)
# # clear all
# numbers.clear()
# print(numbers)
# # find a value in list
# print(1 in numbers)
# # how many elements in the list
# print(len(numbers))

# # for loops
# numbers = [1, 2, 3, 4, 5]
# # loop variable to iterate over items
# for item in numbers:
#     print(item)
#
# # range function
# # object that can store a sequence of numbers
# # excluding 5
# numbers = range(5)
# print(numbers)
# # this doesn't iterate through range use for loop
# for number in numbers:
#     print(number)
# numbers = range(5, 10)
# for number in numbers:
#     print(number)
# # can have third value as a step
# numbers = range(5, 10, 2)
# for number in numbers:
#     print(number)
# # call the function range instead of a separate variable
# for number in range(5):
#     print(number)

# # Tuples, are like list but immutable
# numbers = (1, 2, 3, 3)
# # numbers[0] = 10 will not work
# # count returns number of times its in the tuples
# print(numbers.count(3))
# # index returns first occurrence of given element
# print(numbers.index(2))

