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



if connection.is_connected():

    print("Connection Successful!")

    create_guest_booking("Virvi", "Huta", "virvi@gmail.com", "123456", 1, "2026-06-01", "2026-06-05")

else:
    print("Connection Failed")