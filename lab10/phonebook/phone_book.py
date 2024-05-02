import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phone",
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


# Implement two ways of inserting data into the PhoneBook
while True:
    print("Select the action:\n1)upload data from csv file\n2)enter user name, phone from console\n3)update data in the table\n4)request data from table\n5)delete data from the table\n6)exit")
    action = int(input())

    if action == 1:
        with open('people.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cursor.execute("INSERT INTO phone_book VALUES (%s,%s)", row)
    elif action == 2:
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

        # Implement updating data in the table (change user first name or phone)
    elif action == 3:
        while True:
            print("Change name or number?")
            out = input()
            if out == "name":
                print("Write phone number to change name: ")
                phone = input()
                print("Write name of user:")
                name = input()
                cursor.execute(f"""UPDATE phone_book
                    SET name = '{name}'
                    WHERE phone_number = '{phone}';""")
            else:
                print("Write name to change number: ")
                name = input()
                print("Write phone number:")
                phone = input()
                cursor.execute(f"""UPDATE phone_book
                    SET phone_number = '{phone}'
                    WHERE name = '{name}';""")
            ask = input("Continue?\n")
            if ask == "no":
                break

        # Querying data from the tables (with different filters)
    elif action == 4:
        while True:
            print("Phone, name or all?")
            out = input()
            if out == "name":
                cursor.execute("""SELECT name FROM phone_book""")
                result = cursor.fetchall()
                for row in result:
                    print(row[0])
            elif out == "phone":
                cursor.execute("""SELECT phone_number FROM phone_book""")
                result = cursor.fetchall()
                for row in result:
                    print(row[0])
            elif out == "all":
                cursor.execute("""SELECT * FROM phone_book""")
                result = cursor.fetchall()
                for row in result:
                    name, phone_book = row
                    print(name, phone_book)

            ask = input("Continue?\n")
            if ask == "no":
                break

        # DELETE DATA
    elif action == 5:
        while True:
            cursor.execute("""SELECT * FROM phone_book""")
            result = cursor.fetchall()
            for row in result:
                print(row[0])
            print("Which user to delete?")
            name = input()
            cursor.execute(f"""DELETE FROM phone_book 
                        WHERE name='{name}';""")
            ask = input("Continue?\n")
            if ask == "no":
                break
    elif action == 6:
        break