from calculation import Calculate
from fractions import Fraction

class OutputConverter(Calculate):
    """
    This class is used to convert the output of a calculation to different formats.
    
    Args:
        Calculate (class): The base class for performing calculations.
    """
    def output_format(self, output):
        """
        Converts the output value to the desired format based on user input.

        Args:
            output (float): The output value to be converted.

        Returns:
            str: The converted output value in the selected format.

        Raises:
            ValueError: If an invalid option is chosen by the user.
        """
        print("\033[36mChoose the output format:\033[0m ")
        print("\033[35m1. Round off to two decimal places\033[0m")
        print("\033[35m2. Scientific Notation\033[0m")
        print("\033[35m3. Fraction format\033[0m")
        print("\033[35m4. Default format\033[0m")
        
        option = input("\033[32mInput the corresponding number of your choice (1/2/3/4):\033[0m ")
        
        try:
            if option == "1":
                return "{:.2f}".format(output)
            elif option == "2":
                return "{:.2e}".format(output)
            elif option == "3":
                fraction = Fraction(output).limit_denominator()
                return str(fraction)
            elif option == "4":
                return str(output)
            else:
                raise ValueError("\033[93m: Invalid option xD. Try again!\033[0m")
        except ValueError as raised :
            print(raised)
            return 
        
        finally:
            print("=" * 59)