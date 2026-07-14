import sqlite3
from datetime import datetime


def create_database():

    connection = sqlite3.connect("loan_queries.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS query_history
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_type TEXT,
        query_value TEXT,
        query_time TEXT
    )
    """)

    connection.commit()
    connection.close()



def save_query(query_type, query_value):

    connection = sqlite3.connect("loan_queries.db")

    cursor = connection.cursor()

    current_time = datetime.now()

    cursor.execute(
        """
        INSERT INTO query_history
        (query_type, query_value, query_time)
        VALUES (?, ?, ?)
        """,
        (query_type, query_value, current_time)
    )

    connection.commit()
    connection.close()



def create_application_table():

    connection = sqlite3.connect("loan_queries.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_applications
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        married TEXT,
        dependents TEXT,
        education TEXT,
        self_employed TEXT,
        applicant_income INTEGER,
        coapplicant_income REAL,
        loan_amount REAL,
        loan_term REAL,
        credit_history INTEGER,
        property_area TEXT,
        prediction TEXT
    )
    """)

    connection.commit()
    connection.close()



def save_application(
    gender,
    married,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    property_area,
    prediction
):

    connection = sqlite3.connect("loan_queries.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO loan_applications
    (
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area,
        prediction
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area,
        prediction
    ))

    connection.commit()
    connection.close()