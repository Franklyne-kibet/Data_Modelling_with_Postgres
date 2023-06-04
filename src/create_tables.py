import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """

    Establishes database connection and return's the connection and cursor references.
    :return: return's (cur, conn) a cursor and connection reference
    """
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=my_database user=root password=root port=5431")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb  WITH ENCODING 'utf8' TEMPLATE template0")
    
    # close the connection
    conn.close()
    
    # connect to sparkify database
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=root password=root port=5431")
    cur = conn.cursor()
    
    return cur, conn

def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        
def main():
    """
    Driver main function.
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    print("Tables dropped successfully!")
    
    create_tables(cur, conn)
    print("Tables created successfully!")
    
    conn.close()
    
if __name__ == "__main__":
    main()      