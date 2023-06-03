
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
        self.operation = input("\033[36mChoose one of the operations (Addition, Subtraction, Multiplication, and Division):\033[0m ")  

        
        # ask the user to enter two numbers
        self.num1 = input("\033[32mEnter the 1st number:\033[0m ")
        self.num2 = input("\033[32mEnter the 2nd number:\033[0m ")