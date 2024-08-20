# json_module_example.py
import json

def study_json_module():
    print("JSON Module:")
    # Convert Python object to JSON string
    python_obj = {"name": "Alice", "age": 30, "city": "New York"}
    json_str = json.dumps(python_obj)
    print(f"JSON String: {json_str}")

    # Convert JSON string to Python object
    new_python_obj = json.loads(json_str)
    print(f"Python Object: {new_python_obj}")

if __name__ == "__main__":
    study_json_module()