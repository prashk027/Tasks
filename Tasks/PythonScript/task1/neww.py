import psycopg2
import random
from faker import Faker
 
 
# connection postgreSQL
def connect_db():
    conn = psycopg2.connect(
       host="localhost", dbname="postgres", user="postgres",password = "mypass",port=5431
    )
    return conn
   
# list down schemas
def list_schemas(conn):
    cur = conn.cursor()
    cur.execute("SELECT schema_name FROM information_schema.schemata;")
    schemas = cur.fetchall()
    print("\nAvailable Schemas:")
    for idx, schema in enumerate(schemas):
        print(f"{idx+1}. {schema[0]}")
    schema_idx = int(input("Select Schema (enter number): ")) - 1
    cur.close()
    return schemas[schema_idx][0]
 
#list down tables
def list_tables(conn, schema):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = '{schema}';
    """)
    tables = cur.fetchall()
    print("\nAvailable Tables:")
    for idx, table in enumerate(tables):
        print(f"{idx+1}. {table[0]}")
    table_idx = int(input("Select Table (enter number): ")) - 1
    cur.close()
    return tables[table_idx][0]
 
#list down columns and data type
def get_columns(conn, schema, table):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema='{schema}'
        AND table_name='{table}';
    """)
    columns = cur.fetchall()
    print("\nColumns & DataTypes:")
    for col in columns:
        print(col)
    cur.close()
    return columns
 
# ask for n records to the users
def get_n():
    n = int(input("Enter number of records to insert (1-1000): "))
    if n < 1 or n > 1000:
        raise ValueError("Number of records must be between 1 and 1000.")
    return n
 
 
fake = Faker()
 
first_names = ['Joseph', 'Mark', 'Victor', 'Audrey', 'Kimberly', 'Jessica', 'Annie', 'Thelma', 'Jorge', 'Ronald', 'Travis', 'Jerry', 'Paul', 'Virginia', 'Gertie', 'William', 'Willie', 'Christopher', 'Genevieve', 'Stanley', 'Helen', 'James', 'Bradley', 'Francis', 'Mark', 'Ruben', 'Norma', 'Thelma', 'Betty', 'Linda', 'Sarah', 'Cecilia', 'Edward', 'Lucinda', 'Jack', 'Lisa', 'Julie', 'Joaquin', 'Matthew', 'Rose', 'Colin', 'Danny', 'Carolyn', 'Sammy', 'Louie', 'Amy', 'David', 'Katherine', 'Cora', 'Hector', 'Orlando', 'James', 'Jenny', 'Lori', 'Karen', 'Laura', 'Paul', 'Rebecca', 'Luis', 'Darlene', 'Tiffany', 'Herman', 'Kevin', 'Annie', 'Sharon', 'Enrique', 'Jerome', 'Amber', 'Stephen', 'Iris', 'Susan', 'Amy', 'Johnnie', 'Joseph', 'Javier', 'Jaime', 'Steven', 'Donald', 'Ralph', 'John', 'Nancy', 'Ruth', 'Hilda', 'Robert', 'David', 'Denise', 'Carolyne', 'Barbara', 'Marvin', 'Mary', 'Kimberly', 'Henry', 'Earlie', 'Stephanie', 'Juan', 'Andrea', 'Clifton', 'Lori', 'Richard', 'Johnnie']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
 
def generate_data(columns):
    data = {}
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    for col, dtype in columns:
        if col == 'id':
            continue
        if 'first_name' in col:
            data[col] = fname
        elif 'last_name' in col:
            data[col] = lname
        elif 'email' in col:
            data[col] = f"{fname.lower()}.{lname.lower()}@example.com"
        elif 'age' in col:
            data[col] = random.randint(18, 60)
        elif 'location' in col:
            data[col] = random.choice(locations)
        elif 'contact' in col:
            data[col] = random.randint(10**9, 10**10 - 1)
        elif dtype in ('character varying', 'text', 'varchar'):
            data[col] = fake.word()
        elif dtype in ('integer', 'bigint', 'smallint'):
            data[col] = random.randint(1, 100)
        elif dtype == 'date':
            data[col] = fake.date()
        else:
            data[col] = None
    return data
 
def insert_data(conn, schema, table, columns, n):
    cur = conn.cursor()
    col_names = [col for col, _ in columns if col != 'id']
    placeholders = ', '.join(['%s'] * len(col_names))
    col_string = ', '.join(col_names)
 
    for _ in range(n):
        row = generate_data(columns)
        values = [row[col] for col in col_names]
        cur.execute(f"""
            INSERT INTO {schema}.{table} ({col_string})
            VALUES ({placeholders})
        """, values)
    conn.commit()
    print(f"\nInserted {n} records into {schema}:1{table}")
 
def main():
    conn = connect_db()
    try:
        schema = list_schemas(conn)
        table = list_tables(conn, schema)
        columns = get_columns(conn, schema, table)
        n = get_n()
        insert_data(conn, schema, table, columns, n)
    finally:
        conn.close()
 
if __name__ == "__main__":
    main()
 
   
 
 
 
 
 


























# import psycopg2

# import random

# import re

# from faker import Faker

# # Initialize Faker

# fake = Faker()

# # Hardcoded lists

# FIRST_NAMES = ["John", "Alice", "Robert", "Emily", "Michael", "Sarah"]

# LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]

# DOMAIN = "example.com"

# LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco"]

# # Connect to PostgreSQL


# conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "mypass",port=5431)

# cur = conn.cursor()

# def get_columns(schema, table):

#     """Fetch column names and data types from PostgreSQL table."""

#     cur.execute(f"""

#         SELECT column_name, data_type 

#         FROM information_schema.columns 

#         WHERE table_schema = '{schema}' AND table_name = '{table}';

#     """)

#     return cur.fetchall()

# def match_columns(columns):

#     """Match database columns with expected field names dynamically."""

#     matched = {

#         "first_name": None,

#         "last_name": None,

#         "email": None,

#         "age": None,

#         "contact": None,

#         "location": None

#     }

#     # Define keyword mappings for expected columns

#     column_mapping = {

#         "first_name": ["first_name", "fname", "f_name", "given_name","name"],

#         "last_name": ["last_name", "lname", "l_name", "surname", "family_name"],

#         "email": ["email", "e_mail", "mail"],

#         "age": ["age", "user_age"],

#         "contact": ["contact", "phone", "mobile", "phone_number"],

#         "location": ["location", "city", "place", "residence"]

#     }

#     for col_name, col_type in columns:

#         col_name_lower = col_name.lower()

#         for key, possible_names in column_mapping.items():

#             if any(re.search(rf"\b{keyword}\b", col_name_lower) for keyword in possible_names):

#                 matched[key] = col_name

#     print(matched)
#     return matched

# def generate_valid_data(matched_columns):

#     """Generate valid data based on the matched columns."""

#     row = {}

#     first_name = random.choice(FIRST_NAMES)

#     last_name = random.choice(LAST_NAMES)

#     if matched_columns["first_name"]:

#         row[matched_columns["first_name"]] = first_name

#     if matched_columns["last_name"]:

#         row[matched_columns["last_name"]] = last_name

#     if matched_columns["email"]:

#         row[matched_columns["email"]] = f"{first_name.lower()}.{last_name.lower()}@{DOMAIN}"

#     if matched_columns["age"]:

#         row[matched_columns["age"]] = random.randint(18, 60)

#     if matched_columns["contact"]:

#         row[matched_columns["contact"]] = str(random.randint(6000000000, 9999999999))

#     if matched_columns["location"]:

#         row[matched_columns["location"]] = random.choice(LOCATIONS)

#     return row

# def insert_data(schema, table, columns, n):

#     """Insert N records into the table dynamically based on matched columns."""

#     if not (1 <= n <= 1000):

#         raise ValueError("❌ Error: Number of records must be between 1 and 1000.")

#     matched_columns = match_columns(columns)

#     valid_columns = [col for col in matched_columns.values() if col]

#     print(valid_columns)

#     if not valid_columns:

#         print("❌ No matching columns found in the database!")

#         return

#     for _ in range(n):

#         row = generate_valid_data(matched_columns)

#         columns_list = list(row.keys())

#         values_list = list(row.values())

#         query = f"INSERT INTO {schema}.{table} ({', '.join(columns_list)}) VALUES ({', '.join(['%s'] * len(values_list))})"

#         try:

#             cur.execute(query, values_list)

#         except Exception as e:

#             print(f"Error inserting row: {e}")

#     conn.commit()

#     print(f"✅ {n} records inserted successfully!")

# # User Input

# schema_choice = input("Enter schema name: ")

# table_choice = input("Enter table name: ")

# columns = get_columns(schema_choice, table_choice)

# print("Columns in Table:", columns)

# try:

#     n_records = int(input("Enter number of records to insert (1-1000): "))

#     insert_data(schema_choice, table_choice, columns, n_records)

# except ValueError as e:

#     print(f"❌ Invalid input: {e}")

# # Close connection

# cur.close()

# conn.close()
 