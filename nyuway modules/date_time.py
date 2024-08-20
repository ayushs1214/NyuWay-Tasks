# datetime_module_example.py
import datetime

def study_datetime_module():
    print("Datetime Module:")
    # Get current date and time
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now}")

    # Create a specific date
    specific_date = datetime.date(2024, 8, 7)
    print(f"Specific Date: {specific_date}")

    # Calculate difference between two dates
    delta = datetime.date(2024, 8, 7) - datetime.date(2023, 8, 7)
    print(f"Difference between dates: {delta.days} days")

if __name__ == "__main__":
    study_datetime_module()
