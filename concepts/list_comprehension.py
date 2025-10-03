# list comprehension :: a way to create  new list with less syntax 
#  can mimic certain lamda function ,easier to read 
#1. list = [expression for item in iterable]
#2. list = [expression  for item in iterable if condition ]
#3. list = [expression (if/else) for item in iterable]


# formula :
squares  = []; # crate an empty list 
for i in range (1,11): # crate a for loop 
    squares.append(i*i) # define what each loop iteration should do

print(squares);
## comprehension
squares = [i*i for i in range(1,11)]
# print(squares)

### filtering a list of student grades 

students = [100, 90,70,80,60,50,40,30,0]

passed_students = list(filter(lambda x : x >= 60, students));


passed_students = [i for i in students if i >= 60];

passed_students = [i if i>=60 else "FAILED" for i in students]

print(passed_students);

