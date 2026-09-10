import sqlite3

def init_database():
    # 1.Connect to the database file (this file will be created automatically in your folder). 
    connection = sqlite3.connect("freelance_jobs.db")
    cursor = connection.cursor()

    # 2.Create a new table. 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            budget INTEGER NOT NULL
        )
    """)

    # 3.Insert test data into the database (if the table is empty). 
    cursor.execute("SELECT COUNT(*) FROM projects")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO projects (title, budget) VALUES ('E-commerce Website', 60000)")
        cursor.execute("INSERT INTO projects (title, budget) VALUES ('Python Automation Script', 25000)")
        cursor.execute("INSERT INTO projects (title, budget) VALUES ('Landing Page Design', 15000)")
        connection.commit()
        
    return connection

def fetch_high_budget_projects(connection):
    cursor = connection.cursor()
    # 4. SQL Query Logic: Filter only projects with a budget greater than 20,000.
    cursor.execute("SELECT title, budget FROM projects WHERE budget > 20000")
    
    records = cursor.fetchall()
    print("\n--- 💰Projects with a budget exceeding 20,000  (SQL Filter) ---")
    for row in records:
        print(f"Project: {row[0]} | budget: ₹{row[1]}")

# Main Program
if __name__ == "__main__":
    db_conn = init_database()
    fetch_high_budget_projects(db_conn)
    db_conn.close()