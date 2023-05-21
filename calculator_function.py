import pyfiglet

#define a class that represents the Calculator 
class Calculator:
    def __init__(self, output = "None"):
        #associate output var with a value
        self.output = output
    
    def calc_function(self):
        """It takes the user's inputs for the two numbers and operation to perform, and
        do computation"""
        
        # ask the user to choose one of four math operations:
        self.user_choice_operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Division): ")  
        ## Addition, Subtraction, Multiplication, and Division
        # ask the user to enter two numbers
        self.user_num1 = input("Enter the 1st number: ")
        self.user_num2 = input("Enter the 2nd number: ")
        
        # use Python Functions and appropriate Exceptions to capture errors during runtime.
        try:
            if (self.user_num1.isnumeric() and self.user_num2.isnumeric()):
                self.user_num1 = float(self.user_num1)
                self.user_num2 = float(self.user_num2)  
                # display the result
                if self.user_choice_operation.lower() == "addition":
                    self.output = self.user_num1 + self.user_num2
                elif self.user_choice_operation.lower() == "subtraction":
                    self.output = self.user_num1 - self.user_num2
                elif self.user_choice_operation.lower() == "multiplication":
                    self.output = self.user_num1 * self.user_num2
                elif self.user_choice_operation.lower() == "division":
                    if self.user_num2 == 0:
                        raise ZeroDivisionError("Division by zero is undefined :|")
                    self.output = self.user_num1 / self.user_num2
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
            return self.output
    
    def retry(self):
        while True:
            # ask if the user wants to try again or not.
            self.user_attempt = input("Do you want to try again or not? (yes/no): ")
            
            # if yes, then perform the operation again.
            if self.user_attempt == "yes":
                self.output = self.calc_function()
                print(f"\033[91mResult:\033[0m {self.output}")
                print(".\n.\n.")

            else:
                # if no, Display “Thank you!”
                print(pyfiglet.figlet_format("Thank you!"))
                break      
