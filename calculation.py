from user_input import Input

class Calculate:
    """
    A class that do calculations based on the user's input.
    """
    def calculation(self):
        """
        This function assesses and calculates the value based on the user's input. 
        Once the chosen operation is conducted, the output value is returned. 

        Raises:
            ZeroDivisionError: Raised if the user tries to divide by zero.
            Exception: Raised if an invalid operation is chosen.
            ValueError: Raised if the user enters invalid numbers.

        Returns:
            float: The result of the calculation, or None if an error occurred.
        """
        
        # create the instance of the Input class
        int = Input()
        
        #call the user_input method to get data from the user
        int.user_input()
        
        #associate output var with a value
        output = None
        
        # use Python Functions and appropriate Exceptions to capture errors during runtime.
        try:
            if (int.num1.isnumeric() and int.num2.isnumeric()):
                int.num1 = float(int.num1)
                int.num2 = float(int.num2)  
                
                #perform the mathematical operations
                if int.operation.lower() == "addition":
                    output = int.num1 + int.num2
                elif int.operation.lower() == "subtraction":
                    output = int.num1 - int.num2
                elif int.operation.lower() == "multiplication":
                    output = int.num1 * int.num2
                elif int.operation.lower() == "division":
                    if int.num2 == 0:
                        raise ZeroDivisionError("\033[93m: Division by zero is undefined :|\033[0m")
                    output = int.num1 / int.num2
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
