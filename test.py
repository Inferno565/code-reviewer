# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))


def factorial(n):
    # Initialize the result to 1
    result = 1
    # Calculate factorial
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Enter a number: "))
# Calculate factorial
result = factorial(num)

print(f"The factorial of {num} is {result}")
