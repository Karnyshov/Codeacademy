"""Program imitates Calendar where you can view, add, remove events"""

from time import sleep, strftime

user = "Kyrylo"
calendar = {}


def welcome():
    print("Welcome to the Calendar, " + user + ".")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("Current time is: " + strftime("%H %M %S"))
    sleep(1)

    print("What would you like to do?")

# TODO: Refactor for Python 3
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("A to Add, U to update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()

        if user_choice == "V":
            if calendar.keys() == 0:
                print("No events in Calendar!")
            else:
                print
                calendar
        elif user_choice == "U":
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print("Updated successfully")
            print(calendar)
        elif user_choice == "A":
            event = raw_input("Enter the event: ")
            date = raw_input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("Wrong date!")
                try_again = raw_input("Try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
                    print("Exiting program")
            else:
                calendar[date] = event
                print("Successfully added!")
        elif user_choice == "D":
            if calendar.keys() == 0:
                print("Calendar is already empty!")
            else:
                event = raw_input("What event?")
                for date in calendar.keys():
                    if calendar[date] == event:
                        del calendar[date]
                        print("Event successfully deleted!")
                        print(calendar)
                    else:
                        print("Incorrect event!")
        elif user_choice == "X":
            start = False
            print("Exiting program")
        else:
            print("Invalid command! Exiting the program...")


start_calendar()
