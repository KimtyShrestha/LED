import sqlite3

def add_event(event_name):
    try:
        conn = sqlite3.connect('event_management.db')
        cursor = conn.cursor()

        # Check if the event already exists
        cursor.execute("SELECT * FROM Event WHERE name = ?", (event_name,))
        existing_event = cursor.fetchone()

        if existing_event:
            print(f"Event '{event_name}' already exists.")
        else:
            # Insert the new event into the Event table
            cursor.execute("INSERT INTO Event (name) VALUES (?)", (event_name,))
            conn.commit()
            print(f"Event '{event_name}' added successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)
        print("An error occurred while adding the event.")

    finally:
        conn.close()

# Add events to the database
events_to_add = ["Holi", "Dashain", "Valentines"]

for event in events_to_add:
    add_event(event)

