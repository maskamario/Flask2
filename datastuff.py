import sqlite3

connection = sqlite3.connect('joint.db')

cursor = connection.cursor()

create_agent_table = """CREATE TABLE IF NOT EXISTS
agents(agent_id INTEGER PRIMARY KEY, full_name TEXT, code_name TEXT, phone_number TEXT)"""

cursor.execute(create_agent_table)

create_user_table = """CREATE TABLE IF NOT EXISTS
users(user_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, password TEXT)"""

cursor.execute(create_user_table)

def get_table_rows (table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    results = cursor.fetchall()
    return (results[0][0])

#print (get_table_rows("users"))

def insert_user(firstname, lastname, password):
    rownumber = int(get_table_rows("users")) + 1
    cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?)", (rownumber, firstname, lastname, password))
    #cursor.execute(f"INSERT INTO users VALUES('1', 'Test', 'Testlast', 'Testpassword')")
    connection.commit()
    cursor.execute ( f"SELECT * FROM users WHERE user_id = {rownumber}")
    #cursor.execute ( "SELECT * FROM users WHERE user_id = 1")
    data_request = cursor.fetchall()
    print ("Result of data entry: ", data_request)

#insert_user ('Mirlu', 'Masauskas', 'openpassword')

def get_all_data_from_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    for i in cursor.fetchall():
        print(i)

get_all_data_from_table("users")
#insert_user ('Mirlu', 'Masauskas', 'openpassword')

def delete_all_from_table (table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    tablerows = cursor.fetchall()
    for i in tablerows:
        cursor.execute("")

