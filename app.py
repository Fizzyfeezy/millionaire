
'''list = [2, 4, 3, 5, -5, -3, -4]
total = 0
i = 0
while True:
    if  list[i] < 0:
        break
        total += list[i]
    i+=1
print(total)


total = 0
for element in range(1, 11):
    total += 1
print(element)'''

import json as JSON
import sqlite3 as SQL
import uuid

database_file = "millionaire.db"
sql_connector = SQL.connect(database_file)
cursor = sql_connector.cursor()

sql_file = open("millionaire.sql", "r")
query = sql_file.read()

cursor.execute(query)
question_bank = {1:{'question': 'What is my name','options': {'A': 'kunle', 'B': 'Hafeez', 'C': 'Dave', 'D': 'Lanre'},'answer': 'B'},
                 2: {'question': 'What is my name', 'options': {'A': 'kunle', 'B': 'Hafeez', 'C': 'Dave', 'D': 'Lanre'},
                     'answer': 'B'}}

json_object = JSON.dumps(question_bank)
uuid_to_use = str(uuid.uuid4())

cursor.execute('insert into question_bank(id,question) values(?,?)',[uuid_to_use,json_object])

val = cursor.execute("select * from question_bank;")
print(val.fetchall())
list().__len__()







