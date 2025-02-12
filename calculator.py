import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return Fore.RED + "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def main():
    print(Fore.CYAN + Style.BRIGHT + "Simple Python Calculator")
    print(Fore.YELLOW + "1. Addition (+)")
    print(Fore.YELLOW + "2. Subtraction (-)")
    print(Fore.YELLOW + "3. Multiplication (*)")
    print(Fore.YELLOW + "4. Division (/)")
    print(Fore.YELLOW + "5. Power (^)")

    while True:
        choice = input(Fore.MAGENTA + "Enter choice (1/2/3/4/5) or 'q' to quit: ")

        if choice == 'q':
            print(Fore.GREEN + "Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input(Fore.BLUE + "Enter first number: "))
                num2 = float(input(Fore.BLUE + "Enter second number: "))
            except ValueError:
                print(Fore.RED + "Error: Please enter valid numbers!")
                continue

            if choice == '1':
                print(Fore.GREEN + f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(Fore.GREEN + f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(Fore.GREEN + f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(Fore.GREEN + f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(Fore.GREEN + f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        else:
            print(Fore.RED + "Error: Invalid choice!")

if __name__ == "__main__":
    main()
