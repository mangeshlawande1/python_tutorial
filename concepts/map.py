## map function :: applies a function to each item in an iterable (list , tuple, etc)

# map(function, iterable)

store = [
    ("shirt", 20.00),
    ("pant", 25.00),
    ("t-shirt", 22.00),
    ("jacket", 30.00),
    ("socks", 10.00),
];

to_euros = lambda data:(data[0],data[1]*0.82)
to_dollers = lambda data : (data[0],data[1]/0.82)


store_euros = list(map(to_euros, store))
store_dollers = list(map(to_dollers, store))

for i in store_euros:
    print(i)

for i in store_dollers:
    print(i)