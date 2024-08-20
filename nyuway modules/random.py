# random_module_example.py
import random

def study_random_module():
    print("Random Module:")
    # Generate a random number between 0 and 1
    rand_val = random.random()
    print(f"Random number between 0 and 1: {rand_val}")

    # Generate a random integer between 1 and 10
    rand_int = random.randint(1, 10)
    print(f"Random integer between 1 and 10: {rand_int}")

    # Shuffle a list
    sample_list = [1, 2, 3, 4, 5]
    random.shuffle(sample_list)
    print(f"Shuffled list: {sample_list}")

if __name__ == "__main__":
    study_random_module()