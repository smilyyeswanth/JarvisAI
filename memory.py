import sqlite3

conn = sqlite3.connect(
    "jarvis_memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    key TEXT PRIMARY KEY,
    value TEXT
)
""")

conn.commit()


def remember(key, value):
    cursor.execute(
        """
        INSERT OR REPLACE INTO memory
        (key, value)
        VALUES (?, ?)
        """,
        (key, value)
    )

    conn.commit()


def recall(key):
    cursor.execute(
        """
        SELECT value
        FROM memory
        WHERE key = ?
        """,
        (key,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return None