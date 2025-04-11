import psycopg2
import random
from faker import Faker
import datetime

fake = Faker()

conn = None
cur = None

columns = []

dt_today = datetime.datetime.today()

def generate_random_columns():
    random_element = random.randint(0,8)
    first_name=['Francisco', 'James', 'Kristi', 'Joseph', 'Melissa', 'Rudolph', 'Nora', 'Vincent', 'David']   
    last_name=['Anast', 'Haider', 'Faraone', 'Kendall', 'Bender', 'Cummins', 'Troy', 'Newhall', 'Sessoms']
    age = [random.randint(18,60) for _ in range(9)]
    phone=['7869464740', '7039666521', '9384482158', '8981780373', '8850478561', '8292430729', '7000509463', '7391083379', '9030348021']
    location = [fake.location_on_land()[2] for _ in range(9)]

    return first_name[random_element], last_name[random_element], age[random_element], phone[random_element], location[random_element]

def add_column_timestamp(conn, cur, schema_name, table_name):
    cur.execute(f"""
        select column_name
        from information_schema.columns
        where table_schema = '{schema_name}'
        and table_name = '{table_name}'
        and column_name = 'created_at';
    """)
    if not cur.fetchall():
        cur.execute(f"""
        alter table {schema_name}.{table_name} 
        add column created_at timestamp default '{dt_today.strftime('%Y-%m-%d %H:%M:%S.%f')}';
    """)
        conn.commit()
        print(f"\nAdded column_name created_at in table {table_name}")

    

def get_schema(cur):
    global columns, schema_name, table_name
    '''Method which will get schema, table & respective columns from them'''
    cur.execute('''
                SELECT schema_name 
                FROM information_schema.schemata;
                ''')
    schemas = cur.fetchall()
    
    print("Available Schemas:")
    for schema in schemas:
        print(f">Schema: {schema[0]}")
    
    schema_name = input("\nEnter schema name: ")

    cur.execute(f"""
                select table_name 
                from information_schema.tables 
                where table_schema='{schema_name}';
                """)
    tables = cur.fetchall()
    if tables == []:
        raise IndexError("!!!Please enter correct schema name")
        
    print("\nTable in Schema:")
    for table in tables:
        print(f">Tables: {table[0]}")

    table_name = input("\nEnter table name: ")

    cur.execute(f"""
        select column_name, data_type
        from information_schema.columns
        where table_schema='{schema_name}'
        and table_name = '{table_name}';
        """)
    columns = cur.fetchall()
    if columns == []:
        raise IndexError("!!Please enter correct table name")

    print("\nColumns and Data types: ")
    for column in columns:
        print(f">Columns: {column[0]}: {column[1]}")

    return schema_name, table_name
        

    
def insert_data(columns):
    '''Method which will generate random values which will be inserted into table'''
    data={}
    first_name, last_name, age, phone, location = generate_random_columns()      

    default_items = {
        "last_name":last_name, 
        "contact":phone, 
        "first_name":first_name,
        "age":age,
        "phone":random.randint(1000000001,9999999999),
        "email":f"{first_name.lower()}.{last_name.lower()}@domain.com",
        "location":location,
        "created_at": dt_today.strftime('%Y-%m-%d %H:%M:%S.%f')
    }
            
    for col, d_type in columns:
        if col == 'id':
            continue

        for key,value in default_items.items():
            if key in col:
                data[col] = value
                break

        else:
            if col in default_items:
                data[col] = default_items[col]
            elif d_type in ["character varying", "text", "varchar"]:
                data[col] = fake.word()
            elif d_type in ["integer","bigint","smallint"]:
                data[col] = random.randint(1,100)
            elif d_type == "date":
                data[col] = fake.date()
            else:
                data[col] = None

    return data
        
        

def insert_table(cur,conn, table, schema, colums):
    '''Method which will insert the generated elements into table'''

    n = int(input("Enter number of records to insert (1-1000): "))
    if not (1<=n<=1000):    # value of n is from 1 to 1000
       raise ValueError("Number should be 1-1000")
    col_names = [col for col,_ in colums if col != 'id']   # will not take id from the table
    print(col_names)
    for _ in range(n):  
        row = insert_data(colums)            # will input data and also will map it to the table
        values = [row[col] for col in col_names]
        cur.execute(f"""
                insert into {schema}.{table} ({', '.join(col_names)})
                values ({', '.join(['%s'] * len(col_names))})
        """,values)
    conn.commit()
    print(f"\nInserted {n} records into table: {table} on {dt_today.strftime("%Y-%m-%d %H:%M:%S")}")


try:
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "mypass",port=5431)  # connect to postgres

    cur = conn.cursor()

    schema_name,table_name = get_schema(cur)  # This will give us schema for table
    add_column_timestamp(conn, cur, schema_name,table_name)

    insert_table(cur,conn,table_name,schema_name,columns)    # this method will generate inputs & will insert table in database

    conn.commit()
    
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()