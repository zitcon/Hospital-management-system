import sqlite3

DB_NAME = "hospital.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        role TEXT NOT NULL,
        base_salary REAL NOT NULL,
        extra_value REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        disease TEXT NOT NULL,
        treatment_days INTEGER NOT NULL,
        daily_fee REAL NOT NULL,
        medicine_fee REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()