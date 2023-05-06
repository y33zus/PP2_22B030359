import psycopg2
from config import config



def insert_one_user():

    user_data = input("Give by ',': phone, name, lastname")
    user_data = tuple(user_data.split(","))
    sql = """INSERT INTO phonebook(phone, firstname, lastname) VALUES(%s, %s, %s)"""
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    insert_one_user()