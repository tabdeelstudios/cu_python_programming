# Lists in Python -> ordered and mutable
# person = ['John', 57, 40000.00, True]
#           0     1     2         3   
# print(person)

# for val in person:
#     print(val)
    
# Slicing
# newPerson = person[2:4]
# print(newPerson)

# Length
# print(len(newPerson))

# Mutable
# person[2] = 'Bangalore'
# print(person)

# Concatenation
# firstPersonData = ['Jane', 45]
# secondPersonData = ['Nagpur', 67000.00]
# finalPersonData = firstPersonData + secondPersonData
# print(finalPersonData)

# Sorting
# cities = ["Chennai", "Kolkata", "Bombay", "Jaipur", "Bangalore"]
# print("Before sorting...")
# print(cities)
# sortedCities = cities.sort()
# print("After sorting...")
# print("Cities : ")
# print(cities)
# print("Sorted Cities : ")
# print(sortedCities)

# cities = ["Chennai", "Kolkata", "Bombay", "Jaipur", "Bangalore"]
# print("Before sorting...")
# print(cities)
# sortedCities = sorted(cities)
# print("After sorting...")
# print("Cities : ")
# print(cities)
# print("Sorted Cities : ")
# print(sortedCities)


# Tuple -> ordered and immutable

# person = ('John', 57, 40000.00, True)
# print(person)

# for val in person:
#     print(val)
    
# newPerson = person[1:3]
# print(newPerson)

# person[2] = "Bangalore" -> error
# cities = ("Chennai", "Kolkata", "Bombay", "Jaipur", "Bangalore")
# tempPerson = sorted(cities)
# print(tempPerson)

# Set -> unordered and mutable
# score = {100, 200, 5000}

# score.add(500)
# print(score)

# score1 = {100,200,5000}
# score2 = {100,500,1000}
# print(score1.union(score2))
# print(score1.intersection(score2))
# print(score2.difference(score1))


# Dictionary -> key:value pairs

# person = {
#     'city':'Bangalore',
#     'age':56,
#     'name':'Bob'
# }

# print(person['age'])
# person['age']=70
# print(person)

# person['isEmployed']=True
# print(person)

# print(person.keys())
# for val in person.keys():
#     print(val)
    
# print(person.values())
# for val in person.values():
#     print(val)

#  ----------------------------------------

# Membership
# sentence = "I live in Bangalore"
# print("Chennai" in sentence)
# print("Bangalore" not in sentence)

# Repitition
# error = "Error"
# print(error*10)

# Uppercase / Lowercase
# name = "john"
# print(name.upper())

# name = "JANE"
# print(name.lower())

# Strip
# name = "   John   "
# print(name.strip())

# Counting
# sentence = "I live in Bangalore"
# print(sentence.lower().count('i'))

# Split
# sentence = "I live in Bangalore"
# temp = sentence.split(" ")
# print(temp)

# Formatting
# name = "John"
# age = 56
# occupation = "Teacher"

# output = name + " is " + str(age) + " and he is a " + occupation
# output = '{0} is {1} and he is a {2}'.format(name, age, occupation)
# print(output)

# Multidimensional List
# marks = [[45,46,47], [43,[42,49]], [50,49,43]]
# print(marks[1][1][1])

# Add items to a list
# list = [10,20,30]
# list.append(40)
# print(list)

# Deep Copy / Shallow Copy
# cars = ["BMW", "Audi", "Ford", "McLaren"]
# newCars = cars #Shallow Copy
# newCars = cars[:] #Deep Copy
# newCars[0] = "Jaguar"
# print("New cars : ")
# print(newCars)
# print("Cars : ")
# print(cars)

# -------------------------------------------------

# Map, Filter and Reduce

# Map
# def exponentiate(n):
#     return n*n

# input = [1,2,3,4,5]
# result = map(exponentiate, input)
# print(list(result))

#  Filter
# def isEven(n):
#     if(n%2!=0):
#         return n

# input = [1,2,3,4,5]
# result = filter(isEven, input)
# print(list(result))

# Reduce
# from functools import reduce
# def add(n1,n2):
#     return n1+n2

# marks = [99,89,78,97,65]
# total = reduce(add, marks)
# print(total)

















