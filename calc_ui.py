from calculator_function import Calculator #import Calculator class from calculator function

# create the instance of the Calculator class
ui = Calculator()

# loop to let the user make another attempt
while True:
    # call the calc_function method from  the  ui instance to perform the calculation and print the result
    output = ui.calc_function()
    print(f"\033[91mResult:\033[0m {output}")
    print(".\n.\n.")
    break