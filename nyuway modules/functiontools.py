# functools_module_example.py
import functools

def study_functools_module():
    print("Functools Module:")
    # Using reduce
    sum_val = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(f"Sum using reduce: {sum_val}")

    # Using partial
    def multiply(x, y):
        return x * y

    double = functools.partial(multiply, 2)
    print(f"Double using partial: {double(5)}")

if __name__ == "__main__":
    study_functools_module()