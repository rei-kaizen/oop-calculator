import pyfiglet

#define a class that represents the Calculator 
class Calculator:
    """
    A class that represents the Calculator
    """
    def calc_function(self):
        """This function assesses and calculates the value based on the user's input. 
        First, it asks the user to choose an operation and enter two numbers. 
        Once the chosen operation is conducted, the output value is returned. 

        Raises:
            ZeroDivisionError: Raised if the user tries to divide by zero.
            Exception: Raised if an invalid operation is chosen.
            ValueError: Raised if the user enters invalid numbers.

        Returns:
            float: The result of the calculation, or None if an error occurred.
        """

        # ask the user to choose one of four math operations:
        self.user_choice_operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Division): ")  
        ## Addition, Subtraction, Multiplication, and Division
        # ask the user to enter two numbers
        self.user_num1 = input("Enter the 1st number: ")
        self.user_num2 = input("Enter the 2nd number: ")
        
        #associate output var with a value
        output = None
        
        # use Python Functions and appropriate Exceptions to capture errors during runtime.
        try:
            if (self.user_num1.isnumeric() and self.user_num2.isnumeric()):
                self.user_num1 = float(self.user_num1)
                self.user_num2 = float(self.user_num2)  
                # display the result
                if self.user_choice_operation.lower() == "addition":
                    output = self.user_num1 + self.user_num2
                elif self.user_choice_operation.lower() == "subtraction":
                    output = self.user_num1 - self.user_num2
                elif self.user_choice_operation.lower() == "multiplication":
                    output = self.user_num1 * self.user_num2
                elif self.user_choice_operation.lower() == "division":
                    if self.user_num2 == 0:
                        raise ZeroDivisionError("\033[93m: Division by zero is undefined :|\033[0m")
                    output = self.user_num1 / self.user_num2
                else:
                    raise Exception("\033[93m: Add, Subtract, Multiplication and Division operations only :(\033[0m")
            else:
                raise ValueError("\033[93m: Please enter a valid numbers :)\033[0m")
        
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
    
    def retry(self):
        """
        This function allows the user to retry using the calculator. 
        It asks the user if they would like to try again or quit the program. 
        If the user decides to make another attempt, the calc_function method should be called once more. 
        If the user decides to leave, display a thank-you message .
        """
        # loop to let the user make another attempt
        while True:
            # ask if the user wants to try again or not.
            self.user_attempt = input("Do you want to try again or not? (yes/no): ")
            
            # if yes, then perform the operation again.
            if self.user_attempt == "yes":
                output = self.calc_function()
                print(f"\033[91mResult:\033[0m {output}")
                print(".\n.\n.")

            else:
                # if no, Display “Thank you!”
                print(pyfiglet.figlet_format("Thank you!"))
                break      
