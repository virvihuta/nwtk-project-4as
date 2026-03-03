import mysql.connector

connection = mysql.connector.connect(
    host='htl-datenbank.com',
    port=28474,
    user='virhut23',
    password='REMOVED',
    database='virhut23_hotel_db'
)

if connection.is_connected():
    print("Connection was Successful!")