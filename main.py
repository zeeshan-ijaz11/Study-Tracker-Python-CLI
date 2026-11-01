
from database import (
    create_table,
    add_session,
    view_sessions,
    get_total_minutes
)

running = True

daily_goal = 120

# Create database table
create_table()

while running:

    print("\n================================")
    print("     ENGINEERING STUDY TRACKER")
    print("================================")

    print("\n1. Add Session")
    print("2. View Sessions")
    print("3. Daily Summary")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":

        subject = input("Enter subject: ").strip()

        if subject == "":
            print("Subject cannot be empty!")

        else:
            try:
                minutes = int(input("Enter duration in minutes: "))

                if minutes > 0:
                    add_session(subject, minutes)
                else:
                    print("Minutes must be greater than zero!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "2":

        view_sessions()

    elif choice == "3":

        total_minutes = get_total_minutes()

        progress = (total_minutes / daily_goal) * 100

        print("\n--- DAILY SUMMARY ---")
        print("Total Study Time:", total_minutes, "minutes")
        print("Daily Goal:", daily_goal, "minutes")
        print("Progress:", round(progress, 2), "%")

        if total_minutes >= daily_goal:
            print("Congratulations! Daily goal completed!")

        else:
            print("Keep going! You can reach your goal.")

    elif choice == "4":

        print("Thank you for using Engineering Study Tracker!")
        running = False

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
