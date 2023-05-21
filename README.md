# oop-calculator
This is a oop version of my simple calculator program. Still, it has functions for doing simple mathematical operations, dealing with errors of any kind, and interacting with the user via a command-line interface.

**See sample demo:** <br>
![img](calc-demo.png)

## 📄 Documentation 
<details><summary><h3> 🤔 Usage </h3></summary>

-----

1. Run the program in a Python environment.
2. Choose one of the four math operations: addition, subtraction, multiplication, or division.
3. Enter the first number.
4. Enter the second number.
5. The program will display the result of the operation.
6. You can choose to try again or exit the program.

or

1. Fork this repository 
2. Once the repository has been forked, you can clone the repository to your local machine using the `git clone` command followed by the repository URL.
3. Once the repository is cloned, navigate to the directory of the cloned repository using the `cd` command.
4. Now you can work with the files in the cloned repository.
5. If you want to keep your fork in sync with this repository, you can use the `git fetch` and `git merge` commands to pull in changes and merge them into your local copy.

**Reminders:**
> The program uses appropriate exception handling to capture errors during runtime, such as invalid inputs or division by zero.
</details>

<details><summary><h3> 🔰 Additional information </h3></summary>

-----

**Program: Simple Calculator**
<br>

-The program prompts the user for inputs and provides clear instructions for the chosen operation. 
  
-The `calculator()` function takes no arguments and prompts the user to choose math operations.
  
-This program uses the `pyfiglet` module to have ASCII art representation of **Thank you!** message.<br>
  > This requires the following dependencies to be installed: pyfiglet.<br>
  
-The program uses appropriate exception handling to capture errors during runtime, such as invalid inputs or division by zero. If an error occurs, the program prints a message describing the error and returns None.<br>
  > Exceptions <br>
  ValueError: raised if the user enters an invalid number.<br>
  ZeroDivisionError: raised if the user tries to divide by zero.<br>
  Exception: raised if the user enters an invalid operation.
-


</details>

<details><summary><h3> 💡 Purpose </h3></summary>

-----

The purpose of this program is to provide a basic calculator functionality for simple math operations. It can be used as a reference to understand how to use Python functions and exception handling to build a command-line application.

</details>