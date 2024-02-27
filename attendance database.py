import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('event_management.db')
        cursor = conn.cursor()

        # Create Event table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')

        # Create Attendance table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                event_name TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(event_name) REFERENCES Event(name),
                UNIQUE(student_id, event_name)
            )
        ''')

        print("Database and tables created successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)
        print("An error occurred while creating the database and tables.")

    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
