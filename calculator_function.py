import pyfiglet

while True:
    def calculator():
        """It takes the user's inputs for the two numbers and operation to perform,
        do computation, and displays the result on the screen."""
        # ask the user to choose one of four math operations:
        user_choice_operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Division): ")  
        ## Addition, Subtraction, Multiplication, and Division
        # ask the user to enter two numbers
        user_num1 = input("Enter the 1st number: ")
        user_num2 = input("Enter the 2nd number: ")
        
        
        # use Python Functions and appropriate Exceptions to capture errors during runtime.
        try:
            if (user_num1.isnumeric() and user_num2.isnumeric()):
                user_num1 = float(user_num1)
                user_num2 = float(user_num2)  
                # display the result
                if user_choice_operation == "Addition":
                    output = user_num1 + user_num2
                elif user_choice_operation == "Subtraction":
                    output =user_num1 - user_num2
                elif user_choice_operation == "Multiplication":
                    output =user_num1 * user_num2
                elif user_choice_operation == "Division":
                    if user_num2 == 0:
                        raise ZeroDivisionError("Division by zero is undefined :|")
                    output = user_num1 / user_num2
                else:
                    raise Exception("Add, Subtract, Multiplication and Division operations only :(")
            else:
                raise ValueError("Please enter a valid numbers :)")
        
        except ValueError as raised :
            print(raised)
            return None
            
        except ZeroDivisionError as raised:
            print(raised)
            return None
            
        except Exception as raised:
            print(raised)
            return None

        finally:
            print("=" * 25)
            return output
            
    # Call the function to perform the calculation and print the result
    output = calculator()
    print(f"\033[91mResult:\033[0m {output}")
    print(".\n.\n.")
        
    # use loop to ask if the user wants to try again or not.
    user_attempt = input("Do you want to try again or not? (yes/no): ")
    ## If yes, then perform the operation again.
    ## if no, Display “Thank you!”
    if user_attempt == "no":
        print(pyfiglet.figlet_format("Thank you!"))
        break
    
    # then the program will exit
calculator()