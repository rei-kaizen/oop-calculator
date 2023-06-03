from calculation import Calculate
from output_format import OutputConverter
from retry_function import TryAgain

calc = Calculate()
converter = OutputConverter()
attempt = TryAgain() 

# call the calc_function method from  the  output instance to perform the calculation
output = calc.calculation()

# call the output_forma function from the converter instance to convert output based on user choice
converted_output = converter.output_format(output)
print(f"\033[91mResult:\033[0m {converted_output}")
print(".\n.\n.")

# call the retry function from the attempt instance to allow tthe user to try again
attempt.retry()
