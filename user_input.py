
#define a class that represents the Input of the user 
class Input:
    """
    A class that represents the Input
    """
    def __init__(self):
        self.operation = None
        self.num1 = None
        self.num2 = None
        
    def user_input(self):
        """
        This function asks the user to choose an operation and enter two numbers. 
        """
        # ask the user to choose one of four math operations:
        # Addition, Subtraction, Multiplication, and Division
        self.operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Division): ")  

        
        # ask the user to enter two numbers
        self.num1 = input("Enter the 1st number: ")
        self.num2 = input("Enter the 2nd number: ")
        