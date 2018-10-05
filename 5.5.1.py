# TODO 5.5 passing arguments to Functions
# complete the code below to pass the my_number variable from
# main 3 into square with the parameter name of value remove the """ """ before testing


def main3():
    my_number = 7
    square(my_number)


def square(value):
    squared_value = value * value
    print(squared_value)


main3()
