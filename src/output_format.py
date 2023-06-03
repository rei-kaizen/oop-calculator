from calculation import Calculate
from fractions import Fraction

class OutputConverter(Calculate):
    def output_format(self, output):
        print("Choose the output format:")
        print("1. Round off to two decimal places")
        print("2. Scientific Notation")
        print("3. Fraction format")
        print("4. Default format")
        
        option = input("Input the corresponding number of your choice (1/2/3/4): ")
        
    
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
            print("Invalid option. Try again.")
        
#Testing
output = OutputConverter().calculation() 
converted_output = OutputConverter().output_format(output)
print("Converted Output:", converted_output)