import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phone2",
    user="postgres",
    password="1324"
)
conn.autocommit = True
cursor = conn.cursor()


# create table
# with connection.cursor() as cursor:

# Design tables for PhoneBook.

cursor.execute(
    """CREATE TABLE IF NOT EXISTS phone_book(
        name varchar(50),
        phone_number varchar(20) PRIMARY KEY);"""
)
# conn.commit()

def insert_csv():
        with open('people.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cursor.execute("INSERT INTO phone_book VALUES (%s,%s)", row)

def manual_insert():
    while True:
        print("Write name: ")
        name = input()
        if name == "":
            break
        print("Write number: ")
        phone = input()
        if phone == "":
            break
        cursor.execute(f"""INSERT INTO phone_book (name, phone_number) 
        VAlUES ('{name}', '{phone}');""")
def update_user():
    while True:
        print("Enter name of user to update: ")
        name = input()
        cursor.execute("SELECT * FROM phone_book WHERE name = %s", (name,))
        user_data = cursor.fetchone()

        if user_data:
            print("Enter new phone number: ")
            phone = input()
            cursor.execute("UPDATE phone_book SET phone_number = %s WHERE name = %s", (phone, name))
            print("User information updated successfully.")
        else:
            print("User not found, information was added.")
            phone = input("Enter new phone number:")
            cursor.execute("INSERT INTO phone_book VALUES(%s, %s)", (name, phone))
            ask = input("Continue?\n")
            if ask == "no":
                break

def pattern_quary():
    while True:
        print("Phone or name?")
        out = input()
        if out == "name":
            pattern = input("Enter the pattern: ")
            cursor.execute(f"""SELECT * FROM phone_book
                           WHERE name LIKE '%{pattern}%'""")
            result = cursor.fetchall()
            for row in result:
                name, phone_book = row
                print(name, phone_book)
        elif out == "phone":
            pattern = input("Enter the pattern: ")
            cursor.execute(f"""SELECT * FROM phone_book
                           WHERE phone_number LIKE '%{pattern}%'""")
            result = cursor.fetchall()
            for row in result:
                name, phone_book = row
                print(name, phone_book)

        ask = input("Continue?\n")
        if ask == "no":
            break  

def delete_data():
    while True:
        cursor.execute("""SELECT * FROM phone_book""")
        result = cursor.fetchall()
        for row in result:
            name, phone_book = row
            print(name, phone_book)
        tag = input("Enter username or phone number: ")

        cursor.execute("DELETE FROM phone_book WHERE name = %s OR phone_number = %s", (tag, tag))
        if cursor.rowcount > 0:
            print("User deleted successfully.")
        else:
            print("User not found.")
        ask = input("Continue?\n")
        if ask == "no":
            break
        elif action == 6:
            break 


while True:
    print('''\tSelect the action:
          1)upload data from csv file
          2)enter user name, phone from console
          3)update data in the table
          4)request data from table
          5)delete data from the table
          6)exit''')
    action = int(input())

    if action == 1:
        insert_csv()
    elif action == 2:
        manual_insert()
    elif action == 3:
        update_user()
    elif action == 4:
        pattern_quary()
    elif action == 5:
        delete_data()
    elif action == 6:
        break