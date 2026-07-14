import sqlite3

connection = sqlite3.connect("loan_queries.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM query_history")
rows = cursor.fetchall()

print("Rows:", rows)

connection.close()