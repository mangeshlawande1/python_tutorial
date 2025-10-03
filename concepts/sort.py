## sort method :: used for list 
## sort function ::  used with iterables 

# students = ["squidward", "Sandy","Patrick", "Spongebob", "Mr.Krabs"]

# students.sort(reverse=True)

# for i in students:
#     print(i);


# students = ("squidward", "Sandy","Patrick", "Spongebob", "Mr.Krabs")

# sorted_stud = sorted(students, reverse=True)

# for i in sorted_stud:
#     print(i)

## list of tuples 

# students = [
#     ("squidward", "F", 60),
#     ("Sandy", "A", 33),
#     ("Patrick", "D", 36),
#     ("Spongebob", "B", 20),
#     ("Mr.Krabs", "C", 78)
# ]
# sort student based on grades 

# grade = lambda grades:grades[1]
# students.sort(key = grade)

#  age 
# age = lambda ages: ages[2]
# students.sort(key=age)


# name

# name = lambda names : names[0]
# students.sort(key = name)


# for i in students:
#     print(i);


## tuple of tuples

students = (
    ("squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
);

#  we use sorted function 

age = lambda ages: ages[2]

sorted_students =  sorted(students, key = age)


for i in sorted_students:
    print(i)


