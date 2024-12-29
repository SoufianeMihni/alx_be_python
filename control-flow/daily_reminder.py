# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Initialize the reminder message
    reminder = f"'{task}' is a {priority} priority task"

    # Match case based on priority
    match priority:
        case "high":
            reminder += ". It is important to focus on this task."
        case "medium":
            reminder += ". It should be completed soon."
        case "low":
            reminder += ". Consider completing it when you have free time."
        case _:
            print("Invalid priority entered. Please use high, medium, or low.")
            return

    # Modify reminder if time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound != "no":
        print("Invalid input for time-bound. Please use yes or no.")
        return

    # Print the final reminder
    print("Reminder:", reminder)

# Run the main function
if __name__ == "__main__":
    main()
