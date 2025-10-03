import time

# print(time.ctime(0))
## time converted to readable string 
# time expressed is sec since epoch to a readable string
# epoch = when computer thinks time began (reference point ) 


# print(time.time()) # returns current seconds since epoch

# print(time.ctime(time.time())) ## current time

time_obj = time.localtime()

time_ob = time.gmtime()# universal_time
# print(time_obj);
local_time = time.strftime("%B %d %Y %H:%M:%S",time_obj);
print(local_time)




time_str = "20 April, 2022";

# time_obj = time.strptime(time_str, "%d %B , %Y")
# print(time_obj)

time_tuple = (2020,4,20,4, 20,0,0,0,0)
time_string = time.asctime(time_tuple)
print(time_string)