
---

# Event Booking System

(![image](https://github.com/user-attachments/assets/0a60b67f-c41d-4a2f-84ea-3f7c7f551714)
![image](https://github.com/user-attachments/assets/1f2f900f-6474-4d74-ac3a-c9195c096729)
*A simple command-line application built with Python and MySQL to manage event bookings efficiently.*

---

## Overview
The **Event Booking System** is a Python-based application designed to streamline event management. It allows users to view available events, book tickets, and track their bookings using a MySQL database for persistent storage. This project demonstrates the integration of Python with MySQL for CRUD (Create, Read, Update, Delete) operations in a real-world scenario.

---

## Features
- **View Events**: Display a list of events with details like name, date, and available seats.
- **Book Tickets**: Reserve tickets for an event with real-time seat availability checks.
- **View Bookings**: Retrieve a user’s booking history with event names and dates.
- **Database Integration**: Uses MySQL to store and manage events, users, and bookings.

---

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **MySQL**: [Download MySQL Community Server](https://dev.mysql.com/downloads/)
- **MySQL Connector for Python**: Install via pip (see Installation section).

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/event-booking-system.git
   cd event-booking-system
   ```

2. **Install Python Dependencies**:
   Install the required Python library for MySQL connectivity:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL**:
   Ensure MySQL is running on your system. Update the database connection details in `event_booking.py` if your MySQL username or password differs:
   ```python
   def connect_db():
       return mysql.connector.connect(
           host="localhost",
           user="root",
           password="Megharaj@2004",  # Update this if your password is different
           database="event_booking_system"
       )
   ```

---

## Database Setup
1. **Log in to MySQL**:
   Open your MySQL client (e.g., terminal or MySQL Workbench) and log in:
   ```bash
   mysql -u root -p
   ```
   Enter your password (e.g., `Megharaj@2004`).

2. **Run the Database Script**:
   Copy the contents of `event_booking_database.sql` and execute it in your MySQL client to create the database and tables:
   ```sql
   CREATE DATABASE event_booking_system;
   USE event_booking_system;

   CREATE TABLE events (
       event_id INT AUTO_INCREMENT PRIMARY KEY,
       event_name VARCHAR(100) NOT NULL,
       event_date DATE NOT NULL,
       total_seats INT NOT NULL,
       available_seats INT NOT NULL
   );

   CREATE TABLE users (
       user_id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE
   );

   CREATE TABLE bookings (
       booking_id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT,
       event_id INT,
       tickets_booked INT NOT NULL,
       booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users(user_id),
       FOREIGN KEY (event_id) REFERENCES events(event_id)
   );

   INSERT INTO events (event_name, event_date, total_seats, available_seats)
   VALUES 
       ('Concert Night', '2025-03-15', 100, 100),
       ('Tech Workshop', '2025-03-20', 50, 50);

   INSERT INTO users (username) VALUES ('john_doe');
   ```

3. **Verify Setup**:
   Check that the tables are created and populated:
   ```sql
   SELECT * FROM events;
   SELECT * FROM users;
   ```

---

## Usage
1. **Run the Application**:
   Navigate to the project directory and execute the Python script:
   ```bash
   python event_booking.py
   ```

2. **Interact with the Menu**:
   - **Option 1**: View all available events.
   - **Option 2**: Book tickets for an event by entering the Event ID and number of tickets.
   - **Option 3**: View your booking history.
   - **Option 4**: Exit the application.

   Example:
   ```
   Welcome to the Event Booking System!

   Menu:
   1. View Events
   2. Book Tickets
   3. View My Bookings
   4. Exit
   Enter your choice (1-4): 
   ```

---

## File Structure
```
event-booking-system/
├── event_booking.py         # Main Python script for the application
├── event_booking_database.sql # SQL script to set up the database
└── README.md                # This file
```

---

## Sample Output
### Viewing Events:
```
Available Events:
ID | Name | Date | Seats Available
1 | Concert Night | 2025-03-15 | 100
2 | Tech Workshop | 2025-03-20 | 50
```

### Booking Tickets:
```
Enter Event ID to book: 1
Enter number of tickets: 2
Successfully booked 2 ticket(s) for Event ID 1!
```

### Viewing Bookings:
```
Your Bookings:
Booking ID | Event Name | Tickets | Booking Date
1 | Concert Night | 2 | 2025-02-24 10:00:00
```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a Pull Request.

Feel free to suggest enhancements like a GUI, user authentication, or additional features!

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (you can add a simple MIT license file if needed).

---

### Analysis Notes
- **Python Script (`event_booking.py`)**:
  - Uses `mysql.connector` for database connectivity.
  - Implements basic CRUD operations: read events, create bookings, read bookings.
  - Hardcodes `user_id = 1` for simplicity; future versions could add user authentication.
  - Output is plain text; could be enhanced with libraries like `prettytable` or `colorama`.

- **Database Script (`event_booking_database.sql`)**:
  - Creates a relational database with three tables: `events`, `users`, and `bookings`.
  - Includes foreign key constraints for data integrity.
  - Populates sample data for testing.

