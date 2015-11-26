#!/usr/bin/python
import sqlite3,csv
# def connect_to_db():
# 	conn = sqlite3.connect('test.db')
# 	print "Opened database successfully"

def create_table():
	conn.execute('''CREATE TABLE APRIORITEST4(space_id INT NOT NULL,type_id INT NOT NULL,category_id INT NOT NULL);''')
	print "Table created successfully"

def insert_db():
	conn.execute("INSERT INTO APRIORITEST4(space_id,type_id,category_id) VALUES (22, 44, 66)");
	conn.execute("INSERT INTO APRIORITEST4(space_id,type_id,category_id) VALUES (22, 4, 6)");
	conn.commit()
	print "Done!"

def insert_from_csv():
	with open('Dataset/cleanComplaints.csv','rb') as fin:
		dr = csv.DictReader(fin)
	 	to_db = [(i['space_id'],i['type_id'],i['category_id']) for i in dr]
	conn.executemany("INSERT INTO APRIORITEST4 (space_id,type_id,category_id) VALUES (?, ?, ?);", to_db)
	conn.commit()

def display_db():
	cursor = conn.execute("SELECT * FROM APRIORITEST4")
	for row in cursor:
		print row[0]

conn = sqlite3.connect('test.db')
#create_table()
#insert_db()
#insert_from_csv()
display_db()
conn.close()
