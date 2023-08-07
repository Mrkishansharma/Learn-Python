
try:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    result = num1 / num2

    print(f"The result is: {result}")

except ValueError:

    print("Invalid input. Please enter a valid integer.")

except ZeroDivisionError:
    
    print('divide by zero error')

finally:

    print("This will always execute.")
