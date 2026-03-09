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

if connection.is_connected():
    print("Connection is Successful!")

    cursor = connection.cursor()
    cursor.execute("select * from guests")
    results = cursor.fetchall()
    for i in results:
        print(i)

else:
    print("Connection is not Successful!")