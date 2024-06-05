import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
connection = psycopg2.connect(
    host = "localhost", 
    user = "postgres",
    password = "open",
    database = "salesdata"
)    
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

writer =  connection.cursor()
writer.execute("SELECT version()")
version = writer.fetchone()
print(version)
#connection.close()
#writer.execute("SELECT DATNAME FROM pg_database")
#database = writer.fetchall()
#print(database)
#writer.execute("select table_name from information_schema.tables where table_schema = 'public'")
#Table = writer.fetchall()
#print(Table)
writer.execute("create table Sales1 (emp_id int, name varchar(20), dept varchar(20), salary int)")
#writer.execute("create database salesdata")