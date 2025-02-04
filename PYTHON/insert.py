import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",
    password="", database="db_penjualan")

mycursor= mydb.cursor()
sql= "INSERT INTO kategori(id,name) VALUES (%s,%s)"
val=("29", "Soda")
mycursor.execute(sql,val)


mydb.commit()
print(mycursor.rowcount, "Data berhasil ditambahkan")