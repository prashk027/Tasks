import psycopg2
import numpy as np
import pandas as pd

conn = None
cur = None

def create_derived_table():
    try:
        conn = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password="mypass",port=5431)
        cur = conn.cursor()
        cols = df.columns.to_list()
        table_schema = []
        for i in cols:
            if i == 'id':
                table_schema.append(f'{i} serial primary key')
            elif i == 'name':
                table_schema.append(f'{i} text')
            elif i in ['is_high_quality','is_under_value','is_high_undervalued']:
                table_schema.append(f'{i} boolean')
            else:
                table_schema.append(f'{i} numeric')
    
        cur.execute(f"""
            create table transform_stock(
                {", ".join(table_schema)}
                )
        """)
        conn.commit()

        print("table is created")

    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()

def insert_derived_table(df):
    try:
        conn = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password="mypass",port=5431)
        cur = conn.cursor()
        cols = df.columns.tolist()
        row_data = df.values.tolist()
        
        # insert into table
        for row in row_data:
            cur.execute(f"""
                insert into transform_stock ({', '.join(cols)})
                values ({', '.join(['%s'] * len(cols))})
            """,row)
            conn.commit()
            print("Inserted into stocks table.") 
            

    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()

def get_main_table():
    try:
        conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='mypass', port=5431)
        cur = conn.cursor()

        cur.execute("select * from stocks")
        conn.commit()
        li=[]
        for i in cur.fetchall():
            li.append(i)

        cur.execute("""
            select column_name, data_type
            from information_schema.columns
            where table_schema='public'
            and table_name = 'stocks';
            """)
        columns = cur.fetchall()
        col=[]
        for c,_ in columns:
            col.append(c)
        
        return li, col

    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()

# main code
li,col = get_main_table()
df = pd.DataFrame(li,columns=col)

for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except ValueError:
        continue

df['is_high_quality'] = ((df['roe_percent']>15) & 
        (df['roce_percent']>15) &
        (df['eps_12m_rs']>10) &
        (df['ev_by_ebitda']>10) &
        (df['div_yld_percent']>1) &
        (df['rsi']<70) &
        (df['mar_cap_rscr']>1000))

df['is_under_value'] = ((df['roe_percent']>15) &
        (df['debt_by_eq']<0.5) &
        (df['current_ratio']>2))

df['is_high_undervalued'] = ((df['is_under_value'] == True) & (df['is_high_quality'] == True))


# create_derived_table()
insert_derived_table(df)