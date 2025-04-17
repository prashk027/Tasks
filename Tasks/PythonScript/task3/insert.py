import psycopg2
from main import data

conn = None
cur = None

try:
    conn = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password="mypass",port=5431)
    cur = conn.cursor()
    cols = [col.replace(" ",'_') for col,_ in data.items()]
    cols = [col.replace('%','PERCENT') for col in cols]
    cols = [col.replace('.','') for col in cols]
    cols = [col.replace('/','BY') for col in cols]
    rows = [v for _,v in data.items()]
    cur.execute("select name from stocks")
    conn.commit()
    company_name = []
    for i in cur.fetchall():
        company_name.append(i[0])

    row_data = []
    li =[]

    for row in range(len(rows)):
        for col in range(len(rows[row])):
            for r in range(len(rows)):
                if rows[r][col] == '':
                    li.append(0)
                    continue
                li.append(rows[r][col])
            row_data.append(li)
            li=[]
        break
    
    for row in row_data:
        if row[0] not in company_name:
            print(row[0])
            cur.execute(f"""
                insert into stocks ({', '.join(cols)})
                values ({', '.join(['%s'] * len(cols))})
            """,row)
            conn.commit()
            print("Inserted into stocks table.")
        

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()