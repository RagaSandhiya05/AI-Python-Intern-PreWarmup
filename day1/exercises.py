# T04 - Function-Based Python Exercises


#1. Function to Add Two Numbers
def add_numbers(a, b):
    return a + b

print("#1. Addition")
print("Sum:", add_numbers(10, 20))


#2. Function to Check Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("\n#2. Even or Odd")
print("10 is", check_even_odd(10))
print("7 is", check_even_odd(7))


#3. Function to Find the Square of a Number
def square(number):
    return number * number

print("\n#3. Square of a Number")
print("Square of 5:", square(5))


#4. Function to Find the Largest of Three Numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("\n#4. Largest of Three Numbers")
print("Largest:", find_largest(12, 25, 18))


#5. Function to Calculate Factorial
def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print("\n#5. Factorial")
print("Factorial of 5:", calculate_factorial(5))


#6. Function to Check Prime Number
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

print("\n#6. Prime Number")
print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))


#7. Function to Reverse a String
def reverse_string(text):
    return text[::-1]

print("\n#7. Reverse a String")
print("Reversed:", reverse_string("Python"))


#8. Function to Count Vowels
def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count += 1

    return count

print("\n#8. Count Vowels")
print("Vowels in Python:", count_vowels("Python"))


#9. Function to Find the Average of a List
def calculate_average(numbers):
    if len(numbers) == 0:
        return None

    return sum(numbers) / len(numbers)

print("\n#9. Average of a List")
print("Average:", calculate_average([10, 20, 30, 40, 50]))


#10. Function to Check Palindrome
def is_palindrome(text):
    cleaned_text = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    return cleaned_text == cleaned_text[::-1]

print("\n#10. Palindrome")
print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'python' a palindrome?", is_palindrome("python"))
