import psycopg2

DATABASE_NAME='mytest'
DATABASE_PASSWORD='pw1234'
DATABASE_USER='postgres'
DATABASE_HOST='0.0.0.0'


def database_connection():
    connection = psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD)
    return connection

def seed_csv():
    con = None
    try:    
        connection = database_connection()
        print(connection)
        cursor = connection.cursor()
        print(cursor)

        file = open('data.csv')
        cursor.copy_from(file=file, table=TABLE_NAME, columns=('Id', 'Name', 'Contribution'), sep=",")
        
        cursor.execute('SELECT version()')
        version = cursor.fetchone()[0]
        
        print(version)
        connection.commit()
    except psycopg2.DatabaseError as error:
        print(f'Error {e}', error)
        sys.exit(1)
    finally:
        if connection:
            connection.close()

def select():
    connection = database_connection()
    print(connection)
    cursor = connection.cursor()
    print(cursor)

    try:
        result = cursor.execute('SELECT * FROM test_table')
        print(result)
        print(cursor.fetchone())
        # rows_to_fetch = 3
        # print(cursor.fetchmany(rows_to_fetch))
        # print(cursor.fetchall())
    except Exception as error:
        print(error.message)

def insert():
    connection = database_connection()
    print(connection)
    cursor = connection.cursor()
    print(cursor)
    # result = cursor.execute('INSERT INTO test_table VALUES (123)')
    number = 123
    result = cursor.execute("INSERT INTO test_table (something) VALUES (%s)", ('123',))
    print(result)

def delete():
    connection = database_connection()
    print(connection)
    result = cursor.execute("DELETE * FROM contrib (something) WHERE [123]")
    print(result)
    
# seed_csv()
# select()
# insert()
# delete()