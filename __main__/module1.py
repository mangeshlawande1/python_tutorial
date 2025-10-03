# ************************************************************

# if __name__ =="__main__":

# ************************************************************

## python interpreter sets "special variable", one of which is __name__
#python will assign the __name__ variable a vlaue of '--main--' if it's
# the initial module being run

# import module2
# print(__name__)
# print(module2.__name__)


def hello():
    print("Hello !!");



def say():
    print("Say something !!")


def greet():
    print("welcome to Programming env.")



def main():
    hello();
    say();
    greet();
    print("This function is runs only in current file and not in imported modules ")


if __name__ =="__main__":
    # print("\nrunning this module directly !!\n")
    main()
else:
    # print("running other module indirectly !!\n")
    pass



