import sqlite3

db = sqlite3.connect("database.db")

def cleardb():
    """Clears the database"""
    db.execute("DELETE FROM cat")
    db.commit()
    return "Database cleared!"

cleardb()