import sqlite3
vt = sqlite3.connect("Uyeler.db")
cursor = vt.cursor()

komut = "Create table if not exists Uyelik (ID INTEGER Primary key AUTOINCREMENT, NAME NVARCHAR(30), SURNAME NVARCHAR(30), USERNAME NVARCHAR(30), PASSWORD NVARCHAR(30))"
cursor.execute(komut)
vt.close()


