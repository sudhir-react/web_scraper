import sqlite3

def run_sudhir_database_project():
    print("🚀 Starting Sudhir's Advanced SQLite Database Script...\n")
    
    # 1.Creating and connecting to a database file (preparing the vault)
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # 2.Creating an SQL table (if it does not already exist)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS upwork_jobs (
                job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                budget REAL,
                status TEXT
            )
        ''')
        print("✅ Success: 'upwork_jobs' table verified/created in database.")
        
        # 3. Insert Data using DRY parameters
        sample_jobs = [
            ("Python Trading API Automation", 1500.0, "Reviewed"),
            ("Automated Oil & Gas Glossary Crawler", 55.0, "Proposal Ready"),
            ("Excel Data Scraping Utility", 120.0, "Completed")
        ]
        
        cursor.executemany('''
            INSERT INTO upwork_jobs (job_title, budget, status) 
            VALUES (?, ?, ?)
        ''', sample_jobs)
        
        # Permanently locking (committing) the data in the vault
        conn.commit()
        print(f"✅ Success: {len(sample_jobs)} real-world project records inserted successfully.")
        
        # 4.Retrieving data from the database and displaying it on the screen (Fetch Data)
        print("\n📊 Reading Live Data from 'sudhir_projects.db':")
        print("-" * 50)
        
        cursor.execute("SELECT * FROM upwork_jobs")
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"🆔 Job ID: {row[0]} | 💼 Title: {row[1]} | 💰 Budget: ${row[2]} | 📈 Status: {row[3]}")
            
        print("-" * 50)
        print("\n🎉 SQLite Database execution completed with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Database Error occurred: {e}")
        
    finally:
        # Closing the connection securely
        conn.close()

if __name__ == "__main__":
    run_sudhir_database_project()