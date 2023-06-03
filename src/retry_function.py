import pyfiglet
from calculation import Calculate
from output_format import OutputConverter

class TryAgain():
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
        calc = Calculate()
        converter = OutputConverter()
        
        # loop to let the user make another attempt
        while True:
            # ask if the user wants to try again or not.
            self.user_attempt = input("Do you want to try again or not? (yes/no): ")
            
            # if yes, then perform the operation again.
            if self.user_attempt.lower() == "yes":
                output = calc.calculation()
                converted_output = converter.output_format(output)
                print(f"\033[91mResult:\033[0m {converted_output}")
                print(".\n.\n.")
                
            # if no, Display “Thank you!”    
            elif self.user_attempt.lower() == "no":
                print(pyfiglet.figlet_format("Thank you!"))
                break     
