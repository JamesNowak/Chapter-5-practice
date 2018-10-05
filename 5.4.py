# TODO 5.4 local variables
# Write a program with a main2 function that defines a variable called
# name in the main function, and assign a name to it. Print hello
# and the name variable. Call a second function get_name. In the
# get_name function, ask the user for their name, then greet them
# using a print statement. Be sure to call the main2 function.
# note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in this file.


def main2():

    get_name()


def get_name():

    name = input("What is your name?: ")
    print("Hello,", name + "!")
    main2()
