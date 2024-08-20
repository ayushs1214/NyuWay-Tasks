# re_module_example.py
import re

def study_re_module():
    print("Re Module:")
    # Find all occurrences of a pattern
    text = "The rain in Spain"
    pattern = r'\b\w{4}\b'
    matches = re.findall(pattern, text)
    print(f"Words with 4 letters: {matches}")

    # Replace all occurrences of a pattern
    replaced_text = re.sub(r'rain', 'sun', text)
    print(f"Replaced Text: {replaced_text}")

if __name__ == "__main__":
    study_re_module()
