import sqlite3

def run_database_security_shield():
    print("🛡️ Starting Sudhir's Advanced SQL Injection Shield Test...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # 1. A hacker's malicious input (attempting to wipe out the database)
        hacker_input = "Python Trading API Automation' OR '1'='1" 
        
        # 2. SECURE WAY: Running a query using the '?' security shield.
        print("🔒 Applying Parameterized Shield to neutralize hacker input...")
        secure_query = "SELECT * FROM upwork_jobs WHERE job_title = ?"
        
        # Python will treat the hacker's input as plain text, not as a command!
        cursor.execute(secure_query, (hacker_input,))
        rows = cursor.fetchall()
        
        print("\n🎯 Query Executed Cleanly. Search Results:")
        print("-" * 50)
        if len(rows) == 0:
            print("🛡️ Shield Success: Hack attempt blocked. Zero records leaked.")
        else:
            for row in rows:
                print(f"🆔 ID: {row[0]} | 💼 Title: {row[1]}")
        print("-" * 50)
        
        print("\n🎉 SQL Security Shield execution completed with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Security Failure: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_database_security_shield()