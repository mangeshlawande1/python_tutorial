# walrus operator :=

# new to python 3.8
## assignment expression aka walrus operator
# assign values to variables as part of a larger expssion 

# happy = True
# print(happy)


# print(happy := True)


# foods = list()
# while True:
#     food = input("What food do you like ?: ")
#     if food == "q":
#         break
#     foods.append(food)


# print(foods)

foods = list()
while food := input("What food do you like ?: ") != "q":
    print(food)
    foods.append(food)

print(foods)