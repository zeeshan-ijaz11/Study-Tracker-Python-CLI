
import sqlite3
from datetime import date, datetime


def connect_db():
    connection = sqlite3.connect("study_tracker.db")
    return connection


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            minutes INTEGER NOT NULL,
            study_date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_session(subject, minutes):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions
        (subject, minutes, study_date, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        subject,
        minutes,
        date.today().isoformat(),
        datetime.now().isoformat(timespec="seconds")
    ))

    connection.commit()
    connection.close()

    print("Session saved to database successfully!")


def view_sessions():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sessions ORDER BY id")

    records = cursor.fetchall()

    if len(records) == 0:
        print("No sessions recorded yet.")
    else:
        print("\n--- ALL STUDY SESSIONS ---")

        for session in records:
            print("ID:", session[0])
            print("Subject:", session[1])
            print("Minutes:", session[2])
            print("Date:", session[3])
            print("------------------------")

    connection.close()


def get_total_minutes():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(minutes)
        FROM sessions
        WHERE study_date = ?
    """, (date.today().isoformat(),))

    result = cursor.fetchone()

    connection.close()

    if result[0] is None:
        return 0

    return result[0]


def delete_session(session_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM sessions WHERE id = ?",
        (session_id,)
    )

    connection.commit()

    deleted = cursor.rowcount
    connection.close()

    if deleted > 0:
        print("Session deleted successfully!")
    else:
        print("Session not found!")


if __name__ == "__main__":
    create_table()
    print("Database ready!")
