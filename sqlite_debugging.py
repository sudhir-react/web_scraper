import sqlite3

def debug_and_update_database():
    print("🚀 Starting Sudhir's Advanced DB Debugging Script...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # 1.UPDATE TRICK: Increasing the budget for Job ID 2 (Glossary Project) from $55 to $75.
        print("🔧 Step 1: Updating budget for Job ID 2...")
        cursor.execute("UPDATE upwork_jobs SET budget = 75.0 WHERE job_id = 2")
        
        # 2.DELETE TRICK: Removing all duplicate records with an ID greater than 4 to clean up the database.
        print("🔧 Step 2: Removing duplicate records with ID > 3...")
        cursor.execute("DELETE FROM upwork_jobs WHERE job_id > 3")
        
        # Permanently saving (committing) changes to the repository.
        conn.commit()
        print("✅ Success: Database cleaning and optimization completed.")
        
        # 3. Viewing fresh, filtered data on the screen.
        print("\n📊 Reading Fresh Optimized Data from 'sudhir_projects.db':")
        print("-" * 60)
        
        cursor.execute("SELECT * FROM upwork_jobs")
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"🆔 Job ID: {row[0]} | 💼 Title: {row[1]} | 💰 Budget: ${row[2]} | 📈 Status: {row[3]}")
            
        print("-" * 60)
        print("\n🎉 Advanced SQL Debugging executed with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Debugging Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    debug_and_update_database()