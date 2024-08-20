# loops.py
def for_loop_example():
    print("For Loop Example:")
    for i in range(5):
        print(f"Iteration {i + 1}")
    print()

def while_loop_example():
    print("While Loop Example:")
    count = 0
    while count < 5:
        print(f"Count is {count}")
        count += 1
    print()

def nested_loop_example():
    print("Nested Loop Example:")
    for i in range(3):
        for j in range(2):
            print(f"i = {i}, j = {j}")
    print()

if __name__ == "__main__":
    for_loop_example()
    while_loop_example()
    nested_loop_example()