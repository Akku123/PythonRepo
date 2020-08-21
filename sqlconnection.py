import pyodbc

server = '20.20.1.20'
database = 'X941Q1_DERIVE'
username = 'agupta'
password = 'Admin@12345678'
print("X")


conn = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GTN_TYPE_LOOKUP")
    for row in cursor:
        print(row)
        print()
read(conn)
