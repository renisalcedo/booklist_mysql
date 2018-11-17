from db.db import connectdb

# Will initialize the database Connection
db = connectdb()
db_cursor = db.cursor()

# Column Names
db_props = (db_table, "title", "author", "description")

db_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
db_cursor.execute("USE {}".format(db_name))
db_cursor.execute("CREATE TABLE IF NOT EXISTS {0[0]} \
                    (id INT AUTO_INCREMENT PRIMARY KEY, \
                    {0[1]} VARCHAR(255) NOT NULL, {0[2]} VARCHAR(255) NOT NULL, \
                    {0[3]} VARCHAR(255) NOT NULL)".format(db_props)
                 )