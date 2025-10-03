## zip(*iterables ) = aggregate elements from two or more iterable (list, tuples, sets etc)
# create a zip object with paired elements stored in tuple for each elements for two or more iterables 


username = ["Dude", "Bro", "Mister"]
password = ("p@ssword", "abc123", "Guest@12")
login_date = ["1/2/2021","2/2/2021", "1/2/2021"]
# users =  dict(zip(username, password))

# print(type(users))


# for (key, value) in users.items():
#     print(key," : ", value)

users =  zip(username, password, login_date)
for i in users:
    print(i)