# This program calculates the sum of the first n Fibonacci numbers.

def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    # Get user input
    n = int(input("Enter a positive integer: "))

    # Calculate the sum of the first n Fibonacci numbers
    fib_list = fibonacci(n)
    fib_sum = sum(fib_list)

    # Output the result
    print("The sum of the first", n, "Fibonacci numbers is:", fib_sum)

if __name__ == "__main__":
    main()
    
# This program generates a random password.

import random
import string

def generate_password(length=8):
    """Generate a random password with the given length."""
    password = []
    for i in range(length):
        password.append(random.choice(string.ascii_letters + string.digits))
    return "".join(password)

def main():
    # Get user input
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Output the result
    print("Your random password is:", password)

if __name__ == "__main__":
    main()

# This program finds the average of a list of numbers.

def find_average(numbers):
    """Return the average of the given list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    # Get user input
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or 'q' to quit): "))
        except ValueError:
            break
        numbers.append(num)

    # Find the average
    avg = find_average(numbers)

    # Output the result
    if avg is not None:
        print("The average of the numbers is:", avg)
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
    
# This program converts a decimal number to binary.

def decimal_to_binary(decimal):
    """Convert a decimal number to binary."""
    if decimal == 0:
        return "0b0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return "0b" + binary

def main():
    # Get user input
    decimal = int(input("Enter a decimal number: "))

    # Convert to binary
    binary = decimal_to_binary(decimal)

    # Output the result
    print(decimal, "is equivalent to", binary, "in binary.")

if __name__ == "__main__":
    main()

# This program calculates the factorial of a number.

def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    # Get user input
    n = int(input("Enter a non-negative integer: "))

    # Calculate the factorial
    result = factorial(n)

    # Output the result
    if result is None:
        print("The input must be non-negative.")
    else:
        print(n, "! =", result)

if __name__ == "__main__":
    main()

# This program sorts a list of numbers.

def bubble_sort(numbers):
    """Sort the given list of numbers using bubble sort."""
    n = len(numbers)
    
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

            # Sort the numbers
bubble_sort(numbers)

# Output the result
print("Sorted list:", numbers)
# Calculate the area
area = calculate_area(radius)

# Output the result
print("The area of the circle is:", area)

# Convert to uppercase
uppercase = to_uppercase(s)

# Output the result
print("Uppercase string:", uppercase)

# Calculate the GCD
result = gcd(a, b)

# Output the result
print("The GCD of", a, "and", b, "is:", result)

# Check if n is prime
if is_prime(n):
    print(n, "is prime.")
else:
    print(n, "is not prime.")

# Calculate the square root
result = sqrt(n)

# Output the result
if result is None:
    print("The input must be non-negative.")
else:
    print("The square root of", n, "is:", result)

# Convert to Celsius
temp_c = fahrenheit_to_celsius(temp_f)

# Output the result
print(temp_f, "Fahrenheit is equivalent to", temp_c, "Celsius.")

# Calculate the sum of the squares
result = sum_of_squares(n)

# Output the result
print("The sum of the squares of the first")

# Calculate the factorial
result = factorial(n)

# Output the result
print(n, "! =", result)

# Calculate the sum of the naturals
result = sum_of_naturals(n)

# Output the result
print("The sum of the first", n, "natural numbers is:", result)

# Calculate the area
area = calculate_area(width, height)

# Output the result
print("The area of the rectangle is:", area)

# Check if s is a palindrome
if is_palindrome(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")

# Calculate the factorial
result = factorial(n)

# Output the result
print(n, "! =", result)

# Calculate the sum of the digits
result = sum_of_digits(n)

# Output the result
print("The sum of the digits of", n, "is:", result)

