# from collections import defaultdict
from faker import Faker
import random

faker = Faker()


# names = ['tarun', 'nishant', 'aayush', 'gyan', 'tarun', 'nishant', 'aayush', 'tarun', 'nishant', 'tarun']

# for name in names:
#     freq[name] += 1
# print(freq)
# print(faker.first_name())

const_default = {"first":lambda: faker.first_name(), "last": lambda: faker.last_name()}

for i,v in const_default.items():
    print(i,v())

        # elif "last_name" in col:
        #     data[col] = last_name
        # elif "contact" in col:
        #     data[col] = phone
        # elif "first_name" in col:
        #     data[col] = first_name
        # elif "age" in col:
        #     data[col] = age
        # elif "phone" in col:
        #     data[col] = random.randint(1000000001,9999999999)
        # elif "email" in col:
        #     data[col] = f"{first_name.lower()}.{last_name.lower()}@domain.com"
        # elif "location" in col:
        #     data[col] = location

# from faker import Faker
# import random

# fake = Faker()

# first_name = [fake.first_name() for _ in range(100)]   # using fake library we are generating names 
# last_name = [fake.last_name() for _ in range(100)]
# age = [random.randint(18,60) for _ in range(100)]
# phone = [str(random.randint(1000000000,9999999999)) for _ in range(100)]
# location = [fake.location_on_land()[2] for _ in range(100)]
# print(first_name[random.randint(0,100)])


# import random

# def random_int():
#     return random.randint(100,110)

# age=[]

# for i in range(20):
#     age.append(random_int())

# for i in range(10):
#     age.append(0)

# for i in range(70):
#     age.append(random.randint(1,100))

# print(age)


# first_name=['Francisco', 'James', 'Kristi', 'Joseph', 'Melissa', 'Rudolph', 'Nora', 'Vincent', 'David', 'Todd', 'Felicia', 'Jesus', 'Anthony', 'Kathryn', 'Eva', 'John', 'Arthur', 'Michelle', 'Donna', 'Jerry', 'Stephen', 'John', 'Agnes', 'William', 'Omar', 'Debroah', 'Eleanor', 'Lloyd', 'Brooke', 'Arnold', 'Emily', 'Richard', 'Robert', 'Pamela', 'Rosemarie', 'Jackie', 'Antonio', 'Jeanne', 'Shane', 'David', 'Marcus', 'Rachel', 'Kenneth', 'Warren', 'Roberta', 'Elaine', 'Kendall', 'Eileen', 'Patti', 'Benjamin', 'Bruce', 'Ashley', 'Cynthia', 'Jean', 'Mark', 'Rhonda', 'Ericka', 'Iris', 'Gregory', 'Mildred', 'Jeanetta', 'Damon', 'Deborah', 'Velma', 'Joseph', 'David', 'Norma', 'Muriel', 'Elizabeth', 'Dorothy', 'George', 'Barry', 'Allen', 'Brian', 'Angelica', 'James', 'Sonja', 'Scott', 'Pamela', 'Margaret', 'Dorothy', 'Stewart', 'Ricardo', 'Peggy', 'Efrain', 'Mary', 'Heather', 'Sophie', 'Kristine', 'Violet', 'Thomas', 'Gary', 'Robert', 'Roger', 'Ashley', 'Tori', 'Phyllis', 'Mark', 'Thomas', 'Rebecca', 'Eugene']
# last_name=['Anast', 'Haider', 'Faraone', 'Kendall', 'Bender', 'Cummins', 'Troy', 'Newhall', 'Sessoms', 'Kelly', 'Mendibles', 'Muhlbauer', 'Ericksen', 'Palmer', 'Love', 'Alvarado', 'Richart', 'Bayliff', 'Mathews', 'Fendley', 'Lumpkin', 'Troyer', 'Kenney', 'Cantara', 'Yerkes', 'Ayre', 'Coutee', 'Holmberg', 'Lee', 'Crabtree', 'Hickok', 'Sawer', 'Singh', 'Velasquez', 'Morgan', 'Aspinall', 'Seay', 'Salis', 'Youmans', 'Doran', 'Berndt', 'Long', 'Whitson', 'Robbins', 'Perkins', 'Reaver', 'Ryan', 'Apple', 'Ward', 'Dotson', 'Paxton', 'King', 'Freeman', 'Lewis', 'Pugh', 'Wallace', 'Carbajal', 'Scott', 'Wright', 'Walker', 'Decoteau', 'Macklin', 'Wilson', 'Singleton', 'Knight', 'Bunning', 'Sterback', 'Hunt', 'Todaro', 'Doane', 'Turbacuski', 'Clasby', 'Howlin', 'Gaska', 'Sphon', 'Connelly', 'Mikelson', 'Walker', 'Trickett', 'Calloway', 'Osteen', 'Young', 'Sheridan', 'Langley', 'Ridder', 'Houchins', 'Grimes', 'Musich', 'Rivera', 'Hardy', 'Goode', 'Klocke', 'Stout', 'Perkins', 'Melendez', 'Rivera', 'Polanco', 'Carr', 'Aceuedo', 'Beauregard', 'Wallace']


# li=[]

# for i in range(30):
#     li.append('')

# for i in range(70):
#     em=last_name[random_int()]
#     li.append(em)

# # for i in range(100):
# #     em=first_name[random_int()].lower()+'.'+last_name[random_int()].lower()+'@hotmail.com'
# #     li.append(em)



# print(len(li))
# print(li)






# no='+91'


# mob_li=[]

# def random_int():
#     return random.randint(0,9)

# for i in range(10):
#     mob_li.append('')

# for i in range(20):
#     fi = str(random.randint(7,9))
#     res = [str(random.randint(0,9)) for x in range(7)]
#     no = fi+''.join(res)
#     mob_li.append(no)

# for i in range(70):
#     fi = str(random.randint(7,9))
#     res = [str(random.randint(0,9)) for x in range(9)]
#     no = fi+''.join(res)
#     mob_li.append(no)

# print(len(mob_li))
# print(mob_li)


# import names 

# first_name = []
# last_name = []

# for i in range(100):
#     name = names.get_first_name()
#     lname = names.get_last_name()
#     first_name.append(name)
#     last_name.append(lname)

# # print(first_name)
# print(last_name)