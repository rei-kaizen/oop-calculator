#define a class that represents the Calculator 
class Calculator:
    def calc_function(self):
        """It takes the user's inputs for the two numbers and operation to perform, and
        do computation"""
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
            