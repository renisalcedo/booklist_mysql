from db.db import connectdb

# Will initialize the database Connection
db = connectdb()
db_cursor = db.cursor()
db_name = 'Booklist'
db_table = 'Books'

# Column Names
db_props = (db_table, "title", "author", "description")

db_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
db_cursor.execute("USE {}".format(db_name))
db_cursor.execute("CREATE TABLE IF NOT EXISTS {0[0]} \
                    (id INT AUTO_INCREMENT PRIMARY KEY, \
                    {0[1]} VARCHAR(255) NOT NULL, {0[2]} VARCHAR(255) NOT NULL, \
                    {0[3]} VARCHAR(255) NOT NULL)".format(db_props)
                 )

def print_book_data(req='*'):
    db_cursor.execute("SELECT {} FROM {}".format(req, db_table))
    current_data = db_cursor.fetchall()

    if req == '*':
        print("---------------------- CURRENT DATA --------------------------")
        for col in current_data:
            print("ID: {0[0]}\nTitle: {0[1]}\nAuthor: {0[2]}\nDescription: {0[3]}".format(col))
            print("--------------------------------------------------------------")
    else:
        for col in current_data:
            data = col[0]
            print("{0}: {1}".format(req, data))

def confirm_save():
    confirm = input("Is this correct? [y/n]")
    if confirm == 'y':
        db.commit()
        print(db_cursor.rowcount, " Data Change!")
        print_book_data()
    else:
        print("Data Not Saved!")

def add_book():
    title = input("Input Title: ")
    author = input("Input Author Name: ")
    desc = input("Input Description: ")

    req_body = (title, author, desc)

    db_cursor.execute("INSERT INTO {0[0]} ({0[1]}, {0[2]}, {0[3]}) \
                       VALUES (\"{1[0]}\", \"{1[1]}\", \"{1[2]}\")".format(db_props, req_body))

    print("\n\n")
    print("Title: {0[0]}\nAuthor: {0[1]}\nDescription: {0[2]}".format(req_body))

    confirm_save()

def delete():
    print("-------------- Book Titles --------------")
    print_book_data('title')
    print("-----------------------------------------\n")

    del_book = input("Title of deleting Book: ")
    db_cursor.execute("DELETE FROM {0} WHERE title='{1}'".format(db_table, del_book))

    confirm_save()

def edit_book():
    print_book_data()
    update_book = input("Title of updating Book: ")
    new_data = input("New Data: ")

    update_data = (db_table, 'title', new_data, update_book)
    db_cursor.execute('UPDATE {0[0]} SET {0[1]} = \"{0[2]}\" WHERE {0[1]} = \"{0[3]}\"'.format(update_data))

    confirm_save()

select_switch = {
    1: add_book,
    2: edit_book,
    3: delete,
    4: print_book_data
}

# Run Logic
req = ''
while req != 'q':
    print("Welcome to Book Directory!\n")
    print("1) Add New Book")
    print("2) Edit Book")
    print("3) Remove Book")
    print("4) Print Books")
    print("q) Quit\n")

    req = input("Please Select: ")

    if req != 'q':
        req = int(req)

        if req in select_switch:
            select_switch[req]()
        else:
            print("Invalid Selection")
    else:
        print("Have a nice Day!")

db.close()