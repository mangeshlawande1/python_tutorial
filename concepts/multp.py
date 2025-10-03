# ***************************************
# Python multiprocessing 
# ***************************************
# multiprocessing  = running task in parallel on different cpu cores, bypasses GIL used for the 
# multiprocessing  = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time


def counter(num):
    count =0
    while count<num:
        count+=1



def main():
    # print("")
    a = Process(target=counter, args=(2500000, ))
    b = Process(target=counter, args=(2500000, ))
    d = Process(target=counter, args=(2500000, ))
    c = Process(target=counter, args=(2500000, ))

    # a.start()
    # b.start()
    # c.start()
    # d.start()

    a.join()
    b.join()
    c.join()
    d.join()
    print("finished in :",time.perf_counter(), "seconds")


if __name__=="__main__":
    main()