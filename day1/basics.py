# T03 - Python Fundamentals

#1. Variables and Data Types
name = "Python Intern"
age = 21
cgpa = 8.5
is_learning = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Learning Python:", is_learning)

print(type(name), type(age), type(cgpa), type(is_learning))


#2. Arithmetic Operations
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Remainder:", a % b)
else:
    print("Division by zero is not allowed.")


#3. Check Even or Odd
number = int(input("\nEnter an integer: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


#4. Find the Largest of Three Numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


#5. Multiplication Table
number = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


#6. Find the Factorial of a Number
number = int(input("\nEnter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1

    for i in range(1, number + 1):
        result *= i

    print("Factorial:", result)


#7. Check Prime Number
number = int(input("\nEnter an integer: "))

if number < 2:
    print(number, "is not a prime number")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


#8. Fibonacci Sequence
terms = int(input("\nEnter the number of terms: "))

if terms < 0:
    print("Please enter a non-negative number.")
else:
    a, b = 0, 1

    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b

    print()


#9. List Statistics
numbers = list(map(
    float,
    input("\nEnter numbers separated by spaces: ").split()
))

if not numbers:
    print("The list is empty.")
else:
    print("List:", numbers)
    print("Count:", len(numbers))
    print("Sum:", sum(numbers))
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Average:", sum(numbers) / len(numbers))


#10. Check Palindrome
text = input("\nEnter a word or phrase: ")

cleaned_text = "".join(
    character.lower()
    for character in text
    if character.isalnum()
)

if cleaned_text and cleaned_text == cleaned_text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
