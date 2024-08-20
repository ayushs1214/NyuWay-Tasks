# functions.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(greet("Alice"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Factorial of 5 = {factorial(5)}")