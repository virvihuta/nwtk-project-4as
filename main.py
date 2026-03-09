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
    INSERT INTO guests (first_name, last_name, email, phone)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql_guest, (first_name, last_name, email, phone))
    guest_id = cursor.lastrowid


    sql_booking = """
    INSERT INTO bookings (guest_id, room_id, check_in, check_out)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql_booking, (guest_id, room_id, check_in, check_out))

    connection.commit()

    print("Guest and booking created successfully!")

def bookings_by_date(date):
    sql = """
    select g.first_name, g.last_name, r.room_number, b.check_in, b.check_out from bookings b join guests g on b.guest_id = g.guest_id join rooms r on b.room_id = r.room_id where %s between b.check_in and b.check_out
    """
    cursor.execute(sql, (date,))
    results = cursor.fetchall()
    for i in results:
        print(i)


if connection.is_connected():

    print("Connection Successful!")

    create_guest_booking("Virvi", "Huta", "virvi1@gmail.com", "123456", 1, "2026-06-01", "2026-06-05")
    bookings_by_date("2026-06-02")

else:
    print("Connection Failed")