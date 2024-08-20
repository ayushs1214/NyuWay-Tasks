# collections_module_example.py
import collections

def study_collections_module():
    print("Collections Module:")
    # Using Counter
    counter = collections.Counter([1, 2, 2, 3, 3, 3])
    print(f"Counter: {counter}")

    # Using defaultdict
    def_dict = collections.defaultdict(int)
    def_dict['key1'] += 1
    print(f"DefaultDict: {def_dict}")

    # Using namedtuple
    Point = collections.namedtuple('Point', ['x', 'y'])
    point = Point(10, 20)
    print(f"NamedTuple: {point}")

if __name__ == "__main__":
    study_collections_module()