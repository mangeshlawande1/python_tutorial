# lambda_function :: function are written in 1 line using lambda keyword 
# accept any number of arguments , but only has one expression (think of it as a shortcut )
# (useful if needed for short pariod of time, throw away )

#  lambda parameter : expression 

# def double (x):
#     return x*2

# print(double(5));


double = lambda x : x * 2

print(double(5));
multiply = lambda x, y: x*y

print(multiply(4,5))

add = lambda x,y,z : x+y+z

print(add(1,2,3))

full_name = lambda f_name, l_name : f_name +" "+l_name

print(full_name("Python", "Free"))

age_check = lambda age:True if age>=18 else False

print(age_check(18));