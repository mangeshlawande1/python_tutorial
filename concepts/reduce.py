# reduce :: apply a function to an iterable and reduce it to a single cumulative value 
# performs function on first two elements and repeate process until 1 value remaining

# reduce (function , iterable)

import functools

letters = ['I','T','E','R','A','B','L','E'];


word =  functools.reduce(lambda x,y : x+y, letters);
print(word)

fact = [5,4,3,2,1];

res = functools.reduce(lambda x,y:x*y, fact)

print(res);

