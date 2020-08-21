import pyodbc

server = 'X.X.X.X'
database = 'X'
username = 'X'
password = 'X'
print("X")


conn = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("X")
    for row in cursor:
        print(row)
        print()
read(conn)
