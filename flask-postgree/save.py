import psycopg2

# create routes
# creates services
# creates database structure for pdf


load_csv_to_database():
    
    con = None

    try:
        # con = psycopg2.connect(database='testdb', user='postgres', password='s$cret')
        
        connection = psycopg2.connect(database='mytest', user='postgres', host='0.0.0.0', password='pw1234')
        print(connection)
        cursor = connection.cursor()
        print(cursor)

        file = open('data.csv')
        cursor.copy_from(file=file, table='contrib', columns=('Id', 'Name', 'Contribution'), sep=",")
        
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

    connection = psycopg2.connect(database='mytest', user='postgres', host='0.0.0.0', password='pw1234')
    print(connection)
    cursor = connection.cursor()
    print(cursor)

    try:
        # result = cursor.execute('SELECT * FROM test_table')
        result = cursor.execute('SELECT * FROM contrib')
        print(result)
        print(cursor.fetchone())
        # rows_to_fetch = 3
        # print(cursor.fetchmany(rows_to_fetch))
        # print(cursor.fetchall())
    except Exception as error:
        print(error.message)

def insert():
    connection = psycopg2.connect(database='mytest', user='postgres', host='0.0.0.0', password='pw1234')
    print(connection)
    cursor = connection.cursor()
    print(cursor)
    # result = cursor.execute('INSERT INTO test_table VALUES (123)')
    number = 123
    result = cursor.execute("INSERT INTO test_table (something) VALUES (%s)", ('123',))
    print(result)

def delete():
    connection = psycopg2.connect(database='mytest', user='postgres', host='0.0.0.0', password='pw1234')
    print(connection)
    result = cursor.execute("DELETE * FROM contrib (something) WHERE [123]")
    print(result)
    
# load_csv_to_database()
select()