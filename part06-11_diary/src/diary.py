# Write your solution here

# Read any existing diary entries from file
with open("diary.txt", "r") as new_file:
    entries = new_file.readlines()

# Start main loop
while True:
    # Prompt user for action
    print("1 - add an entry, 2 - read entries, 0 - quit")
    action = input("Function: ")

    # Add new entry
    if action == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as new_file:
            new_file.write(entry + "\n")
        print("Diary saved")

    # Read existing entries
    elif action == "2":
        print("Entries:")
        for entry in entries:
            print(entry.strip())

    # Quit program
    elif action == "0":
        print("Bye now!")
        break

    # Handle invalid input
    else:
        print("Invalid input. Please enter 1, 2, or 0.")