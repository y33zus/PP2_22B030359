import psycopg2
import csv
from config import config

def insert_many_users():
    sql = "INSERT INTO phonebook(phone, firstname, lastname) VALUES(%s, %s, %s)"
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        csv_filename = 'users.csv'
        with open(csv_filename) as f:
            reader = csv.reader(f)
            list_of_users = list(tuple(line) for line in reader)

        print(list_of_users)
        cur.executemany(sql, list_of_users)
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    insert_many_users()