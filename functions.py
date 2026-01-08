def greet(first_name, last_name):
    print("Hi there")
    print("Welcome aboard")
    print(f"Hi {first_name} {last_name}")

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


greet("Pedro", "Miranda")
print(multiply(2, 3, 4, 5))