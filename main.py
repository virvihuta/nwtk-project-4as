import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(override=True)

user = os.getenv("user")
password = os.getenv("password")

connection = mysql.connector.connect(
    host='htl-datenbank.com',
    port=28474,
    user=user,
    password=password,
    database='virhut23_hotel_db'
)

cursor = connection.cursor()

def create_guest_booking(first_name, last_name, email, phone, room_id, check_in, check_out):
    sql_guest = """
    insert into guests (first_name, last_name, email, phone)
    values (%s, %s, %s, %s)
    """

    cursor.execute(sql_guest, (first_name, last_name, email, phone))
    guest_id = cursor.lastrowid

    sql_booking = """
    insert into bookings (guest_id, room_id, check_in, check_out)
    values (%s, %s, %s, %s)
    """

    cursor.execute(sql_booking, (guest_id, room_id, check_in, check_out))
    booking_id = cursor.lastrowid

    connection.commit()

    print("\n==============================")
    print("booking created successfully")
    print("==============================")
    print(f"guest name   : {first_name} {last_name}")
    print(f"email saved  : {email}")
    print(f"phone saved  : {phone}")
    print(f"guest id     : {guest_id}")
    print(f"booking id   : {booking_id}")
    print(f"room id      : {room_id}")
    print(f"check in     : {check_in}")
    print(f"check out    : {check_out}")
    print("==============================\n")


def bookings_by_date(date):
    sql = """
    SELECT g.first_name, g.last_name, r.room_number, b.check_in, b.check_out
    FROM bookings b
    JOIN guests g ON b.guest_id = g.guest_id
    JOIN rooms r ON b.room_id = r.room_id
    WHERE %s BETWEEN b.check_in AND b.check_out
    """

    cursor.execute(sql, (date,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"{row[0]} {row[1]} | Room {row[2]} | {row[3]} → {row[4]}")
    else:
        print("No bookings found for this date.")


def add_service_to_booking(booking_id, service_id):
    sql = """
    INSERT INTO booking_services (booking_id, service_id)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (booking_id, service_id))
    connection.commit()

    print("Service added to booking!")


def cancel_bookings(booking_id):
    sql = """
    DELETE FROM bookings
    WHERE booking_id = %s
    """

    cursor.execute(sql, (booking_id,))
    connection.commit()

    print("Booking cancelled!")



def menu():
    while True:
        print("\n===== HOTEL MANAGEMENT SYSTEM =====")
        print("1 - Create guest and booking")
        print("2 - Show bookings by date")
        print("3 - Add service to booking")
        print("4 - Cancel booking")
        print("5 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            room_id = int(input("Room ID: "))
            check_in = input("Check-in date (YYYY-MM-DD): ")
            check_out = input("Check-out date (YYYY-MM-DD): ")

            create_guest_booking(first_name, last_name, email, phone, room_id, check_in, check_out)

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            bookings_by_date(date)

        elif choice == "3":
            booking_id = int(input("Booking ID: "))
            service_id = int(input("Service ID: "))
            add_service_to_booking(booking_id, service_id)

        elif choice == "4":
            booking_id = int(input("Booking ID to cancel: "))
            cancel_bookings(booking_id)

        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Invalid option. Try again.")


if connection.is_connected():
    print("Connection Successful!")
    menu()

else:
    print("Connection Failed")