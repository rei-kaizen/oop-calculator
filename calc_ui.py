from calculator_function import Calculator #import Calculator class from calculator function

# create the instance of the Calculator class
ui = Calculator()

# call the calc_function method from  the  ui instance to perform the calculation and print the result
output = ui.calculation()
print(f"\033[91mResult:\033[0m {output}")
print(".\n.\n.")

# call the retry function from the ui instance to allow tthe user to try again
ui.retry()
