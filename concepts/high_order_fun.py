## higher order function  = a function that either :
        # 1. accept a function as arguments
# or
# 2. return a function as  output (python function treated as an objects )

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Higher Order function");
#     print(text)


# hello(loud)
# hello(quiet)

## higher order


def divisor(x):
    def dividend(y):
        return y/x
    return dividend


# divide = divisor(9)

# print(divide(2))


divide = divisor(3)

print(divide(9))