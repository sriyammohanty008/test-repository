import psycopg2
def create_table():
    conn=psycopg2.connect("dbname='sriyam' user='postgres' password='crackwhack2' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ITEM(item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
        conn=psycopg2.connect("dbname='sriyam' user='postgres' password='crackwhack2' host='localhost' port='5432' ")
        cur=conn.cursor()
        ##cur.execute("INSERT INTO ITEM VALUES(%s,%s,%s)",(item,quantity,price))
        cur.execute("INSERT INTO ITEM VALUES('%s','%s','%s')" %(item,quantity,price))
        conn.commit()
        conn.close()

def delete(item):
    conn=psycopg2.connect("dbname='sriyam' user='postgres' password='crackwhack2' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("DELETE FROM ITEM WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
        conn=psycopg2.connect("dbname='sriyam' user='postgres' password='crackwhack2' host='localhost' port='5432' ")
        cur=conn.cursor()
        cur.execute("UPDATE ITEM SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
        conn.commit()
        conn.close()

insert("apple",10,15)
update("apple",10,45)
