# Hotel Booking System

simple python console application that interacts with a mysql database to manage a hotel booking system.

the program allows creating guests, creating bookings, adding services to bookings, viewing bookings for a specific date, and cancelling bookings.

## features

- create a guest and booking
- view bookings for a specific date
- add services to a booking
- cancel bookings
- interactive menu system
- mysql database integration

## database structure

the system uses the following tables:

guests  
stores guest information

rooms  
stores hotel room information

services  
stores available hotel services

bookings  
stores booking records linking guests and rooms

booking_services  
junction table that connects bookings with services

## requirements

- python 3
- mysql server
- mysql-connector-python
- python-dotenv

install dependencies:

pip install mysql-connector-python python-dotenv

## environment variables

create a `.env` file with your database credentials:

user=your_mysql_user  
password=your_mysql_password

## running the program

run the program with:

python main.py

if the connection is successful, a menu will appear:

1 create guest and booking  
2 show bookings by date  
3 add service to booking  
4 cancel booking  
5 exit

## example workflow

1 create a guest and booking  
2 view bookings for a date  
3 add services to a booking  
4 cancel a booking if needed

## notes

- booking ids are generated automatically by the database
- foreign key constraints ensure data integrity
- deleting a booking automatically deletes related booking services

## author

Virvi Huta
