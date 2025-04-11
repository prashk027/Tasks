import psycopg2
import random

first_name=['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','Rhonda', 'Richard', 'John', 'Barry', 'Roberta', 'Eva', 'Agnes', 'Donna', 'Eugene', 'Vincent', 'David', 'Angelica', 'Sophie', 'Mark', 'Kathryn', 'George', 'Violet', 'Ericka', 'Dorothy', 'Margaret', 'Eileen', 'Jackie', 'Peggy', 'Vincent', 'Jesus', 'James', 'Ricardo', 'Vincent', 'Agnes', 'Efrain', 'Marcus', 'Debroah', 'Marcus', 'James', 'Pamela', 'Violet', 'Norma', 'George', 'Cynthia', 'Thomas', 'Antonio', 'Phyllis', 'Brian', 'Brian', 'Mark', 'Roger', 'Peggy', 'Pamela', 'John', 'Peggy', 'Kristi', 'Scott', 'Donna', 'Elaine', 'Angelica', 'Joseph', 'Lloyd', 'Allen', 'Sophie', 'Efrain', 'Eileen', 'Bruce', 'Eleanor', 'Mark', 'Violet', 'Ashley', 'Joseph', 'Kendall', 'Warren', 'Cynthia']

last_name=['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Richart', 'Kenney', 'Turbacuski', 'Whitson', 'Doran', 'Sphon', 'Osteen', 'Robbins', 'Rivera', 'Faraone', 'Singh', 'Perkins', 'Scott', 'Connelly', 'Wallace', 'Dotson', 'Mathews', 'Knight', 'Howlin', 'Decoteau', 'Alvarado', 'Calloway', 
'Gaska', 'Sterback', 'Perkins', 'Wallace', 'Coutee', 'Hunt', 'Hickok', 'Mathews', 'Ridder', 'Singh', 'Wallace', 'Grimes', 'King', 'Bunning', 'Velasquez', 'Aspinall', 'Faraone', 'Bayliff', 'Young', 'Houchins', 'Polanco', 'Beauregard', 'Haider', 'Young', 'Kendall', 'Reaver', 'Salis', 'Ward', 'Carbajal', 'Sphon', 'Bunning', 'Pugh', 'Rivera', 'Kendall', 'Decoteau', 'Paxton', 'Turbacuski', 'Walker', 'Osteen', 'Klocke', 'Musich', 'Ridder', 'Hardy', 'Dotson', 'Perkins', 'Wallace', 'Fendley', 'Salis']

phone=['', '', '', '', '', '', '', '', '', '', '89638112', '79224746', '86316076', '79886175', '87874016', '89969025', '79149270', '80345410', '86588401', '99774617', '86206814', '78184344', '95984977', '91486742', '89450023', '87261025', '90071217', '93312316', '70019577', '89924151', '9080779119', '7516936501', '7192743819', '9706568542', '7878963558', '9513539350', '8570858046', '7804673772', '7401574898', '9559980551', '7935583888', '7611928955', '7271788388', '7746951345', '8405678822', '7779347191', '8159002266', '7268538315', '9171471729', '9232520126', '9240757030', '8329665551', '9167244800', '9831763898', '7656908209', '7258759763', '9248153250', '7466022633', '7242114256', '7463806520', '7498625387', '8618817602', '9093609573', '7833665263', '9813943366', '7523757402', '9024599984', '8465909933', '9005872117', '9296279281', '7583077413', '9647800691', '7509060658', '8192544209', '8776731208', '7847420028', '9715089642', '9149333493', '8321067344', '9797073570', '7589474253', '8880187236', '9804406921', '9531738975', '7435427137', '9201608373', '8572768945', '8510034580', '8449333513', '8808313066', '7899509102', '8543053141', '9725494312', '9964314162', '7118503869', '7112469477', '7637529259', '7737210737', '8439959212', '7385145508']


age=[105, 108, 108, 107, 109, 101, 100, 102, 101, 108, 108, 104, 101, 106, 106, 102, 101, 100, 101, 105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 77, 88, 39, 3, 23, 10, 30, 37, 95, 69, 2, 36, 83, 4, 6, 100, 19, 32, 71, 77, 75, 60, 64, 28, 48, 37, 11, 70, 91, 56, 52, 16, 19, 4, 2, 78, 95, 97, 84, 56, 1, 99, 6, 69, 76, 7, 81, 96, 37, 17, 45, 77, 61, 48, 93, 91, 91, 29, 48, 75, 84, 76, 12, 75, 68, 10, 81, 9, 26]

samples_list=[]

valid_entry=[]

conn = None
cur = None


def rand_int():
    return random.randint(0,99)

def chemail(f,l):
    mail='@hotmail.com'
    first = first_name[f].lower()
    last = last_name[l].lower()
    if first=='' and last=='':
        return 'Invalid Entry'
    elif first == '' and last !='':
        return last.lower()+mail
    elif first != '' and last=='':
        return first.lower()+mail
    else:
        return first.lower()+'.'+last.lower()+mail

for i in range(10):
    f=rand_int()
    l=rand_int()
    samples_list.append({'first_name':first_name[f],
     'last_name':last_name[l],
     'phone':phone[rand_int()],
     'age':age[rand_int()],
     'email':chemail(f,l)
     }
    )

print(samples_list)

# random int from the sample list 
# def random_int():
#     return random.randint(0,4)

def check_valid():
    ind=random.randint(0,4)
    first_name = samples_list[ind]['first_name']
    last_name = samples_list[ind]['last_name']
    mobile = samples_list[ind]['phone']
    age = samples_list[ind]['age']
    email = samples_list[ind]['email']

    if len(mobile)==10 and first_name != '' and last_name != '' and (age>0 and age<100) and email != 'Invalid Entry':
        entery=(first_name, last_name, age, email, mobile)
        valid_entry.append(entery)
        return first_name, last_name, age, email,mobile
        # return mobile
    elif len(mobile) != 10:
        return 'mobile'
    elif first_name == '':
        return 'first_name'
    elif last_name == '':
        return 'last_name'
    elif email == '':
        return 'email'
    elif (age<0 and age>100):
        return 'age'
    else:
        return 'all'


try:

    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "mypass",port=5431)

    cur = conn.cursor()

    create_table = '''
    CREATE TABLE
    STUDENTS (
        ID Serial PRIMARY key,
        F_NAME VARCHAR(255) DEFAULT NULL,
        L_NAME VARCHAR(255) DEFAULT NULL,
        AGE varchar(10),
        EMAIL VARCHAR(255) DEFAULT NULL,
        PHONE VARCHAR(13) DEFAULT NULL
    );
    '''

    insert_script='''
        insert into students(f_name,l_name,age,email,phone) values(%s,%s,%s,%s,%s);
    '''

    # cur.execute(create_table)   # only use when you have to create table
    
    val=check_valid()
    print(val)

    # for i in range(2):
    #     val=check_valid()
    #     print(val,valid_entry)
    # print(type(val),val[0],val[1],val[2],val[3])
    # print(val)
    
    if type(val)==tuple:
        print(0)
        # insert_values=[(lis[1]['first_name'],lis[0]['last_name'],val),('Rudolph','look',val)]

        for ent in valid_entry:
            insert_values=(ent[0],ent[1],ent[2],ent[3],ent[4])
            # insert_values=('Violet', 'Singh', '95', 'thomas@hotmail.com','9171471729')
            print(insert_values)
            cur.execute(insert_script,insert_values)
            # for record in insert_values:
            #     cur.execute(insert_script,record)
        print("Succesfull.")

    else:
        print(f'Invalid {val} entry')
        

    # cur.execute(insert_script,insert_values)
    # cur.execute('SELECT * FROM stud')
    # rows = cur.fetchall()

    
    # for row in rows:
    #     print(row)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()