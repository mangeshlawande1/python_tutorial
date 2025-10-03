# filter :: create a collection of elements from an iterablefor which a function return true

# filter(function, iterable )

### drinking age for a 


friends = [
    ("Rachel",19),
    ("Ravi",22),
    ("Monika",18),
    ("Phoebe",17),
    ("Joey",16),
    ("Chandler",21),
    ("Ross",20)
]

age = lambda data:data[1] >= 18

# create a separate collections 
drinking_buddies = list(filter(age,friends))



for i in drinking_buddies:
    print(i)




