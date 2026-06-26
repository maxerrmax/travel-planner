import sqlite3

DB_NAME = "travel_plans.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itineraries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination TEXT NOT NULL,
            days INTEGER NOT NULL,
            preferences TEXT NOT NULL,
            plan TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def save_itinerary(destination, days, preferences, plan):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO itineraries (destination, days, preferences, plan)
        VALUES (?, ?, ?, ?)
    """, (destination, days, preferences, plan))

    conn.commit()
    conn.close()

def get_all_itineraries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, destination, days, preferences, created_at
        FROM itineraries
        ORDER BY created_at DESC
    """)

    itineraries = cursor.fetchall()

    conn.close()

    return itineraries

def get_itinerary_by_id(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT destination, days, preferences, plan
        FROM itineraries
        WHERE id = ?
    """, (id,))

    itinerary = cursor.fetchone()

    conn.close()

    return itinerary