# thread = a flow of execution . like a separate order of instructions.
# however each thread takes a turn running to cheieve concurrency'
# #GIL = (Global Interpreter Lock) --> 1 thread runs at 1 time 

#  allows only one thread to hold the control of the python interpreter at any 1 time

# cpu bound =  program/task spends most of it's time waiting for internal events(CPU)
            # use multiprocessing 

# io bound = program /task spends most of the time waiting for external events (user inputs, web scrapping)
# use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3);
    print("You eat brakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank, Coffee")


def study():
    time.sleep(5)
    print("You finish study !!")


# eat_breakfast()
# drink_coffee()
# study()

## perform multitasking concurrently
x = threading.Thread(target=eat_breakfast, args =())
x.start()

y = threading.Thread(target=drink_coffee, args=());
y.start()

z = threading.Thread(target=study, args=())
z.start()


x.join()
y.join()
z.join()

print(time.perf_counter())
print(threading.active_count());
print(threading.enumerate());

