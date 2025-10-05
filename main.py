# Railway-Reservation-System
trains = [
    {"no": 101, "name": "Express A", "seats": 3},
    {"no": 102, "name": "Express B", "seats": 2},
    {"no": 103, "name": "Express C", "seats": 1},
]

tickets = {}

# Show Trains Function
def show_trains():
    print("\nAvailable Trains:")
    for train in trains:
        print(f"Train No: {train['no']}, Name: {train['name']}, Seats available: {train['seats']}")

# Book Ticket Function
def book_trains():
    tno = int(input("\nEnter Train Number to book: "))
    name = input("Enter Passenger Name: ")
    for train in trains:
        if train["no"] == tno and train["seats"] > 0:
            train["seats"] -= 1
            tickets[name] = tno
            print(f"✅ Ticket booked successfully for {name} in Train {train['name']}")
            return
    print("❌ Booking failed! Train not found or no seats available.")

# Cancel Ticket Function
def cancel_ticket():
    name = input("\nEnter Passenger Name to Cancel Ticket: ")
    if name in tickets:
        tno = tickets[name]
        for train in trains:
            if train["no"] == tno:
                train["seats"] += 1
                del tickets[name]
                print(f"✅ Ticket cancelled successfully for {name}")
                return
    print("❌ No booking found for this passenger!")

# View Ticket Function
def view_ticket():
    name = input("\nEnter Passenger Name to View Ticket: ")
    if name in tickets:
        tno = tickets[name]
        for train in trains:
            if train["no"] == tno:
                print(f"Passenger: {name}, Train: {train['name']}, Train No: {tno}")
                return
    print("❌ No ticket found for this passenger.")

# Main Menu Function
def main_menu():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Show Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Ticket")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_trains()
        elif choice == 2:
            book_trains()
        elif choice == 3:
            cancel_ticket()
        elif choice == 4:
            view_ticket()
        elif choice == 5:
            print("🙏 Thank you for using Railway Reservation System!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the program
main_menu()
