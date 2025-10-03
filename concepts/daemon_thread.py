## daemon thread = a thread taht runs in the background, not important for program to run,
        # your program will not wait for daemon thread  to complete before exiting 
# non-daemon thread cannot normally be killed , stay alived until task is completed 
# ex used for background tasks , garbage collection, waiting for input , long running processes
#  


import threading
import time



def timer():
    print("")
    count =0;
    while True:
        time.sleep(1)
        count+=1
        print(f"Logged in for {count} seconds")


x = threading.Thread(target=timer, daemon = True)
x.start()

# x.setDaemon(True)

answer = input("Do you with to exit ?:")
# @@ warning @@  dont try at your machine 