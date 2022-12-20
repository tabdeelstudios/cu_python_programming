# print("Hello world")

# dynamically typed
# age = int(input("Enter your age : "))
# print("Your age is : " + str(age))

# num1=10
# num2=4

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1**num2)
# num1+=num2
# num1 = num1 + num2

# Decision Making
# billAmount = float(input("Enter the total bill : "))
# discount = 0

# if billAmount > 5000.00:discount=20
# elif billAmount > 4000.00:discount=15
# elif billAmount > 3000.00:discount=10
# elif billAmount > 2000.00:discount = 5
# else:discount=0
    
# print("Your total discount is : "+str(discount)+"%")


# billAmount = float(input("Enter the total bill : "))
# # if billAmount > 5000.00:print("20% discount")

# # shorthand if-else

# print("20% discount") if billAmount > 5000.00 else print("No discount")

# Loops

cartItems = int(input("How many items in the cart? : "))

while cartItems>0:
    print("You still have "+str(cartItems)+" items in the cart!")
    cartItems = cartItems-1

print("Your cart is empty")

# Lists

cities = ["Mumbai", "Pune", "Chennai", "Bangalore"]

for city in cities:
    print(city)

for c in "Hello":
    print(c+"\n")
    
for num in range(10,20):
    print(num)














