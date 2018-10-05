# TODO 5.8 value returning functions
# Complete the following program, remove the """  """ before testing


def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds"))
    answer = bmi(height, weight)  # TODO call the bmi function and assign the result to a variable named answer

    print("Your BMI is", format(answer, ".1f"))  # TODO print the variable answer, make sure to format it to 1 decimal place

    # TODO modify the bmi function to accept the height and weight
    # read the code to determine the parameter names


def bmi(weight_pounds, height_inches):
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi = (weight_pounds / (height_inches * height_inches)) * 703
    return patient_bmi  # TODO send the patient_bmi value back to main6


main6()
