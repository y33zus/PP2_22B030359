import psycopg2
from config import config


def create_table():
    """ create tables in the PostgreSQL database"""
    conn = None
    try:    
        commands = (
            """
            CREATE TABLE users (
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(32) NOT NULL,
                user_level INTEGER NOT NULL,
                user_speed INTEGER NOT NULL
            )
            """,
            """ CREATE TABLE users_scores (
                    user_id INTEGER PRIMARY KEY,
                    user_score INTEGER NOT NULL,
                    FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
                )
            """
        )       
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()