from calculation import Calculate
from retry_function import TryAgain

# create the instance of the Calculate class
calc = Calculate()

# create the instance of the TryAgain class
attempt = TryAgain() 

# call the calc_function method from  the  ui instance to perform the calculation and print the result
output = calc.calculation()
print(f"\033[91mResult:\033[0m {output}")
print(".\n.\n.")

# call the retry function from the ui instance to allow tthe user to try again
attempt.retry()
