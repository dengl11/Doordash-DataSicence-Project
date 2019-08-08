###########################################################
###############        SQlite Ops         #################
###########################################################
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def send_query(conn, query):
    """send a query via a connection
    Args:
        conn: 
        query: 

    Return: 
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def get_columns(conn, table):
    """return an array of column names from table
    Args:
        conn: 
        table: 

    Return: 
    """
    cursor = conn.execute('select * from {}'.format(table))
    return [description[0] for description in cursor.description]
    

def get_table_names(conn):
    """return table names from a sqlite connection
    
    Args:
        conn: 

    Return: 
    """
    tables = send_query(conn, "SELECT name FROM sqlite_master WHERE type='table'")
    return list(tables)


def get_rows(conn, table):
    """return all rows from a table
    
    Args:
        conn: 

    Return: 
    """
    rows = send_query(conn, "SELECT * FROM {}".format(table))
    return rows
