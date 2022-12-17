import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="root", database= "cms")

command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print(" ")
        print("Admin Menu")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")

        option = str(input("Option: "))
        if option == "1":
            print(" ")
            print("Register New Student")
            username = str(input("Enter Username: "))
            password = str(input("Enter Password: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (Username, Password, Privilege) VALUES(%s, %s,'Student')",query_vals)
            db.commit()
            print(username + " has been registered as a student")

        elif option == "2":
            print(" ")
            print("Register New Teacher")
            username = str(input("Enter Username: "))
            password = str(input("Enter Password: "))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (Username, Password, Privilege) VALUES(%s, %s,'Teacher')",
                                    query_vals)
            db.commit()
            print(username + " has been registered as a teacher")

        elif option == "3":
            print(" ")
            print("Delete Existing Student")
            username = str(input("Enter Username: "))

            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE Username = %s AND Privilege = %s",
                                    query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been removed")

        elif option == "4":
            print(" ")
            print("Delete Existing Teacher")
            username = str(input("Enter Username: "))

            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE Username = %s AND Privilege = %s",
                                    query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been removed")

        elif option == "5":
            break
        else:
            print("Invalid Option Selected")
def auth_admin():
    print(" ")
    print("Admin Login")
    print(" ")
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))
    if user_name == "admin":
        if password == "admin":
            admin_session()
        else:
            print("Incorrect password. Try again!!!")
    else:
        print("Unauthorized Login")
def main():
    while 1:
        print("Welcome to College Management System")
        print(" ")
        print("1. Login as Teacher")
        print("2. Login as Student")
        print("3. Login as Admin")

        option = str(input("Enter an option "))
        if option == "1":
            print("Teacher Login")
        elif option == "2":
            print("Student Login")
        elif option == "3":
            auth_admin()
        else:
            print("Invalid choice")

main()