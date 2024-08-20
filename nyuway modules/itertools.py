# itertools_module_example.py
import itertools

def study_itertools_module():
    print("Itertools Module:")
    # Using count
    counter = itertools.count(start=10, step=2)
    print(f"Count: {next(counter)}, {next(counter)}, {next(counter)}")

    # Using permutations
    perm = itertools.permutations([1, 2, 3])
    print(f"Permutations: {list(perm)}")

    # Using combinations
    comb = itertools.combinations([1, 2, 3], 2)
    print(f"Combinations: {list(comb)}")

if __name__ == "__main__":
    study_itertools_module()