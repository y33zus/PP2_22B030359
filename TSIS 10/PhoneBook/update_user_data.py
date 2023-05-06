import psycopg2
from config import config

def update_user_data(person_id, person_phone="", person_name=""):
    #в зависимости от входных данных
    if person_phone == "":
        sql = """ UPDATE phonebook
            SET firstname = %s
            WHERE person_id = %s"""
    elif person_name == "":
        sql = """ UPDATE phonebook
            SET phone = %s
            WHERE person_id = %s"""
    else:
        sql = """ UPDATE phonebook
            SET phone = %s,
            SET firstname = %s
            WHERE person_id = %s"""
    
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if person_phone == "":
            cur.execute(sql, (person_name, person_id))
        elif person_name == "":
            cur.execute(sql, (person_phone, person_id))
        else:
            cur.execute(sql, (person_phone, person_name, person_id))

        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    update_user_data(person_phone="+77771112233", person_id=3)