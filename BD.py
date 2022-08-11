import psycopg2

with psycopg2.connect(database="HWSQL5", user="alciona", password="alciona") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE phones;
            DROP TABLE client;
            """)

# Функция, создающая структуру БД (таблицы)

def create_db(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS client(
        client_id INTEGER UNIQUE PRIMARY KEY,
        first_name VARCHAR(60),
        last_name VARCHAR(60),
        email VARCHAR(60)
        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER REFERENCES client(client_id),
        phone VARCHAR(11)
        );""")
    conn.commit()  # фиксируем в БД

# Функция, позволяющая добавить нового клиента

def add_client(conn, client_id, first_name, last_name, email, phones=None):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO client(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);
    """, (client_id, first_name, last_name, email))
    conn.commit()
    cur.execute("""
    SELECT * FROM client;
    """)
    print(cur.fetchall())
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phones))
    conn.commit()
    cur.execute("""
    SELECT * FROM phones;
    """)
    print(cur.fetchall())

 # Функция, позволяющая добавить телефон для существующего клиента

def add_phone(conn, client_id, phone):
    cur = conn.cursor()
    cur.execute("""
    UPDATE phones SET phone=%s WHERE client_id=%s;
    """, (phone, client_id))
    conn.commit()  # фиксируем в БД

# Функция,позволяющая удалить телефон для существующего клиента
def delete_phone(conn, client_id, phone):
    cur.execute("""
            DELETE FROM phones WHERE id=%s;
            """, (1,))
    cur.execute("""
            SELECT * FROM phones;
            """)
    print(cur.fetchall())


def delete_client(conn, client_id):
    cur.execute("""
                DELETE FROM client WHERE id=%s;
                """, (1,))
    cur.execute("""
                SELECT * FROM client;
                """)
    print(cur.fetchall())

# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
            INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s);
            """, (2, "задание посложнее", python_id))
    conn.commit()  # фиксируем в БД

conn.close()