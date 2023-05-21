import pyfiglet
from calculator_function import Calculator #import Calculator class from calculator function

# create the instance of the Calculator class
ui = Calculator()

# call the calc_function method from  the  ui instance to perform the calculation and print the result
output = ui.calc_function()
print(f"\033[91mResult:\033[0m {output}")
print(".\n.\n.")
    
# use loop to ask if the user wants to try again or not.
user_attempt = input("Do you want to try again or not? (yes/no): ")
## If yes, then perform the operation again.
## if no, Display “Thank you!”
if user_attempt == "no":
    print(pyfiglet.figlet_format("Thank you!"))
    break
