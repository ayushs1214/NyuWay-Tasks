# main.py
import loops
import functions
import anonymous_functions

def main():
    print("Executing Loop Examples:")
    loops.for_loop_example()
    loops.while_loop_example()
    loops.nested_loop_example()
    
    print("Executing Function Examples:")
    print(functions.greet("Bob"))
    print(f"5 + 7 = {functions.add(5, 7)}")
    print(f"Factorial of 6 = {functions.factorial(6)}")
    
    print("Executing Anonymous Function Examples:")
    numbers = [1, 2, 3, 4, 5]
    print(f"Squared numbers: {anonymous_functions.square_numbers(numbers)}")
    
    numbers = [10, 15, 22, 35, 40]
    print(f"Even numbers: {anonymous_functions.filter_even(numbers)}")
    
    pairs = [(3, 4), (1, 2), (5, 0)]
    print(f"Sorted by second element: {anonymous_functions.sort_by_second_element(pairs)}")

if __name__ == "__main__":
    main()