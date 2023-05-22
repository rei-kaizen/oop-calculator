import pyfiglet
from calculation import Calculate

class TryAgain:
    """
    A class that let the user to retry the calculation.
    """
    def retry(self):
        """
        This function allows the user to retry using the calculator. 
        It asks the user if they would like to try again or quit the program. 
        If the user decides to make another attempt, the calc_function method should be called once more. 
        If the user decides to leave, a thank-you message is displayed.
        """
        calc2 = Calculate()
        
        # loop to let the user make another attempt
        while True:
            # ask if the user wants to try again or not.
            self.user_attempt = input("Do you want to try again or not? (yes/no): ")
            
            # if yes, then perform the operation again.
            if self.user_attempt == "yes":
                output = calc2.calculation()
                print(f"\033[91mResult:\033[0m {output}")
                print(".\n.\n.")
                
            # if no, Display “Thank you!”    
            elif self.user_attempt == "no":
                print(pyfiglet.figlet_format("Thank you!"))
                break     