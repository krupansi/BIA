import mysql.connector

conn=mysql.connector.connect(host='localhost', username='root', password='Krupa@2112', database='test');
if conn.is_connected():
    print("Successfully Connected..")
    
    
cs=conn.cursor()

Q1= f"""INSERT INTO Employee (FirstName, LastName, Age, Department, City, Salary) Values
('Karina', 'Savaliya', '22', 'Data Analytics', 'Pune', '35000.00');"""
cs.execute(Q1)

Q2= f"""INSERT INTO Employee (FirstName, LastName, Age, Department, City, Salary) Values
('Mantr', 'Hirpara', 26, 'ML', 'Vapi', 62000.00);"""
cs.execute(Q2)
print("Record Insert Successfully")


#cs.execute("DELETE FROM Employee WHERE FirstName='Mantr';")

cs.execute("SELECT * FROM Employee;")
r1=cs.fetchall()
for i in r1:
    print(i)

conn.commit()
conn.close()