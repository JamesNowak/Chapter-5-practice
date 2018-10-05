# TODO 5.7 value returning functions
# Add a statement importing the random library at the top of this file
# Add the global constant PI with a value of 3.14 before the main5 function
import random
pi = 3.14


def main5():
    r = random.randint(1, 10)
    r2 = r * r
    area(r2)


def area(r2):
    my_area = pi * (r2)
    print(format(my_area, ",.2f"))


main5()
