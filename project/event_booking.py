import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="Megharaj@2004",  
        database="event_booking_system"
    )

def display_events():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT event_id, event_name, event_date, available_seats FROM events"
    cursor.execute(query)
    events = cursor.fetchall()
    print("\nAvailable Events:")
    print("ID | Name | Date | Seats Available")
    for event in events:
        print(f"{event[0]} | {event[1]} | {event[2]} | {event[3]}")
    cursor.close()
    conn.close()

def book_tickets(user_id):
    display_events()
    event_id = int(input("Enter Event ID to book: "))
    tickets = int(input("Enter number of tickets: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT available_seats FROM events WHERE event_id = %s", (event_id,))
    available_seats = cursor.fetchone()[0]

    if tickets > available_seats:
        print("Not enough seats available!")
    else:
        new_seats = available_seats - tickets
        cursor.execute("UPDATE events SET available_seats = %s WHERE event_id = %s", (new_seats, event_id))
        
        cursor.execute(
            "INSERT INTO bookings (user_id, event_id, tickets_booked) VALUES (%s, %s, %s)",
            (user_id, event_id, tickets)
        )
        conn.commit()
        print(f"Successfully booked {tickets} ticket(s) for Event ID {event_id}!")
    
    cursor.close()
    conn.close()


def view_bookings(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT b.booking_id, e.event_name, b.tickets_booked, b.booking_date 
        FROM bookings b 
        JOIN events e ON b.event_id = e.event_id 
        WHERE b.user_id = %s
    """
    cursor.execute(query, (user_id,))
    bookings = cursor.fetchall()
    if bookings:
        print("\nYour Bookings:")
        print("Booking ID | Event Name | Tickets | Booking Date")
        for booking in bookings:
            print(f"{booking[0]} | {booking[1]} | {booking[2]} | {booking[3]}")
    else:
        print("No bookings found.")
    cursor.close()
    conn.close()

def main():
    print("Welcome to the Event Booking System!")
    user_id = 1 
    while True:
        print("\nMenu:")
        print("1. View Events")
        print("2. Book Tickets")
        print("3. View My Bookings")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_events()
        elif choice == "2":
            book_tickets(user_id)
        elif choice == "3":
            view_bookings(user_id)
        elif choice == "4":
            print("Thank you for using the Event Booking System!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()