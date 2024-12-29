# pattern_drawing.py

def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Use a while loop for rows
        row = 0
        while row < size:
            # Use a for loop for columns
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after a row is complete
            row += 1

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Run the main function
if __name__ == "__main__":
    main()
