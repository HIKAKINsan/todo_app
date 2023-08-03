import os, psycopg2, string

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def insert_todo(todo, deadline, priority):
    sql = 'INSERT INTO todo VALUES(default, %s, %s, %s, false)'
    
    try :
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(sql,(todo, deadline, priority))
        
        count = cursor.rowcount
        connection.commit()
        
    except psycopg2.DatabaseError:
        count = 0
    finally:
        cursor.close()
        connection.close()
        
    return count

def select_todo():
    sql = 'SELECT * FROM todo WHERE complate_flg = false ORDER BY priority ASC'
    
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return rows