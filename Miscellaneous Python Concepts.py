#Membership

# sentence = "I live in Bangalore"

# print("Bangalore" in sentence)
# print("Bangalore" not in sentence)

#Repitition
# error = "Error"
# print(error*10)

#Uppercase / Lowercase
# name="john"
# print(name.upper())

# name="JANE"
# print(name.lower())

# name = "  John  "
# print(name.strip())

# sentence = "I live in Bangalore"
# print(sentence.lower().count('i'))

# sentence = "I live in Bangalore"
# temp = sentence.split(" ")
# print(temp)

# name = "John"
# occupation = "Teacher"
# city = "Bangalore"
# output = '{0} is a {1} and he lives in {2}'.format(name, occupation, city)
# print(output)

# Multidimensional List
# marks = [[45,44,[36,76]], [50,45,44]]
# print(marks[0][2])

# # Concatenate Lists
# list1 = [10,20,30]
# list2 = [50,60,70]
# list3 = list1+list2
# print(list3)

# #Repition
# print(list3*5)

#Add items to a list
# list = [10,20,30]
# print(list)
# list.append('H')
# print(list)

#Sort
# cars = ["BMW", "Audi", "McLaren", "Mercedes", "Ford"]
# sortedCars = cars.sort()
# print("original - " + str(cars))
# print("sorted - " + str(sortedCars))

# Sorted
# cars = ["BMW", "Audi", "McLaren", "Mercedes", "Ford"]
# sortedCars = sorted(cars)
# print(cars)
# print(sortedCars)

# Shallow Copy / Deep Copy

# cars = ["BMW", "Audi", "McLaren", "Mercedes", "Ford"]
# # newCars = cars # Shallow Copy
# newCars = cars[:] # Deep Copy
# print(cars)
# print(newCars)

# newCars[0]="Jaguar"
# print("----------------")
# print(cars)
# print(newCars)

# Map, Filter and Reduce

# Map
def exponentiate(n):
    return n*n
input = [1,2,3,4,5]
result = map(exponentiate, input)
print(list(result))

# Filter
def isEven(n):
    if(n%2!=0):
        return n
input = [1,2,3,4,5]
result = filter(isEven, input)
print(list(result))

# Reduce
from functools import reduce
def add(n1,n2):
    return n1+n2
input = [1,2,3,4,5]
sum = reduce(add, input)
print(sum)



