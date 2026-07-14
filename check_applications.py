import sqlite3

connection = sqlite3.connect("loan_queries.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM loan_applications")

applications = cursor.fetchall()

if len(applications) == 0:
    print("No applicant details found in database.")
else:
    print("Stored Applicant Details:")
    print("-------------------------")

    for row in applications:
        print(row)

connection.close()