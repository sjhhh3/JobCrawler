import sqlite3

cn = sqlite3.connect("testdb.db")
cursor = cn.cursor()

def create_table(cn, cursor):
    cursor.execute("""
		CREATE TABLE amazonjb(
			ID serial Primary key,
			JOB_ID INT,
			NAME VARCHAR,
			LOC VARCHAR,
			DEP VARCHAR,
			ABB VARCHAR,
			DES TEXT,
			REQ TEXT,
			PRF TEXT)
    		   """)
    cn.commit()

def read(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
        print('\n')

def insert_item(data):
    sql = ("""INSERT INTO amazonjb \
		(JOB_ID, NAME, LOC, DEP, ABB, DES, REQ, PRF) VALUES \
		(?, ?, ?, ?, ?, ?, ?, ?);""")
    cursor.execute(sql, data)
    cn.commit()


if __name__ == "__main__":
    #insert_item((12345, "Name", "Loc", "Dep", "Abb", "Des", "Req", "Prf"))
    #read("SELECT * FROM amazonjb")
    #create_table(cn, cursor)
    pass
