 
import psycopg2
import random
from faker import Faker
 
fake = Faker()
conn = None
cur = None
columns = []
 
 
def get_schema(cur):
    """Method to get schema, table & respective columns"""
    global columns, schema_name, table_name
 
    cur.execute("SELECT schema_name FROM information_schema.schemata;")
    schemas = cur.fetchall()
   
    print("Available Schemas:")
    for schema in schemas:
        print(f"- {schema[0]}")
   
    schema_name = input("\nEnter schema name: ")
 
    cur.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema='{schema_name}';")
    tables = cur.fetchall()
 
    if not tables:
        raise IndexError("!!!Please enter a correct schema name")
   
    print("\nTables in Schema:")
    for table in tables:
        print(f"- {table[0]}")
 
    table_name = input("\nEnter table name: ")
 
    cur.execute(f"""
        SELECT column_name, data_type FROM information_schema.columns
        WHERE table_schema='{schema_name}' AND table_name='{table_name}';
    """)
    columns = cur.fetchall()
 
    if not columns:
        raise IndexError("!!Please enter a correct table name")
 
    print("\nColumns and Data types:")
    for column in columns:
        print(f"- {column[0]}: {column[1]}")
 
 
def check_email(first_name,last_name):
    """Generates an email based on available names."""
    first = False
    last = False
    val = ''
    for col,_ in columns:
        if ('first_name' in col) or ('last_name' in col):
            last=True
            if first & last:
                val = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
            elif 'first_name' in col:
                val = f"{first_name.lower()}@gmail.com"
                first = True
            elif 'last_name' in col:
                val = f"{last_name.lower()}@gmail.com"
            else:
                val = 'Not Avaliable'
        else:
            continue 
    return val

 
 
def insert_data(columns):
    """Method to generate random values to be inserted into the table"""
    data = {}
 
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 60)
    phone = str(random.randint(1000000000, 9999999999))
    location = fake.city()

 
    for col, d_type in columns:
        if col == 'id':
            continue
        elif "last_name" in col:
            data[col] = last_name
        elif "contact" in col or "phone" in col:
            data[col] = phone
        elif "first_name" in col:
            data[col] = first_name
        elif "age" in col:
            data[col] = age
        elif "email" in col:
            data[col] = check_email(first_name,last_name)  
        elif "location" in col:
            data[col] = location
        elif d_type in ["character varying", "text", "varchar"]:
            data[col] = fake.word()
        elif d_type in ["integer", "bigint", "smallint"]:
            data[col] = random.randint(1, 100)
        elif d_type == "date":
            data[col] = fake.date()
        else:
            data[col] = None
 
    return data
 
 
def insert_table(cur, conn, table, schema, columns):
    """Method to insert generated elements into the table"""
    try:
        n = int(input("Enter number of records to insert (1-1000): "))
        if not (1 <= n <= 1000):
            raise ValueError("Number should be between 1 and 1000")
 
        col_names = [col for col, _ in columns if col != 'id']  
 
        for _ in range(n):
            row = insert_data(columns)  # Generate data
            values = [row[col] for col in col_names]
 
            cur.execute(f"""
                INSERT INTO {schema}.{table} ({', '.join(col_names)})
                VALUES ({', '.join(['%s'] * len(col_names))});
            """, values)
 
        conn.commit()
        print(f"\nInserted {n} records into {table}")
 
    except Exception as error:
        print("Error inserting data:", error)
 
 
try:
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "mypass",port=5431)  # connect to postgres

 
    cur = conn.cursor()
    get_schema(cur)  # Get schema, table & columns
    insert_table(cur, conn, table_name, schema_name, columns)  # Insert data
 
except Exception as error:
    print("Database Connection Error:", error)
 
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
 
 