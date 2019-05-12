# Python program for implementation
# of Bisection Method for
# solving equations


# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2  + 2


def func(x):
    return x*x - (3 * x)  + 2

# Prints root of func(x)
# with error of EPSILON


def bisection(a, b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b-a) >= 0.01):

        c = (a+b)/2

        if (func(c) == 0.0):
            break

        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c

    print("Akar nya adalah : ", "%.4f" % c)


a = 1
b = 2
bisection(a, b)
