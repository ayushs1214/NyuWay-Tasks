# anonymous_functions.py
def square_numbers(numbers):
    square = lambda x: x ** 2
    return list(map(square, numbers))

def filter_even(numbers):
    is_even = lambda x: x % 2 == 0
    return list(filter(is_even, numbers))

def sort_by_second_element(pairs):
    pairs.sort(key=lambda x: x[1])
    return pairs

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Squared numbers: {square_numbers(numbers)}")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Even numbers: {filter_even(numbers)}")
    
    pairs = [(1, 3), (4, 1), (2, 2)]
    print(f"Sorted by second element: {sort_by_second_element(pairs)}")