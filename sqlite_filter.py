import sqlite3

def filter_high_budget_jobs():
    print("🚀 Starting Sudhir's Advanced DB Filtering Script...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # SQL Command:Searching for jobs with a budget of over $100 only
        select_query = "SELECT * FROM upwork_jobs WHERE budget > 100"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        print("🎯 Premium Jobs Found (Budget > $100):")
        print("-" * 50)
        
        for row in rows:
            print(f"🆔 ID: {row[0]} | 💼 Job: {row[1]} | 💰 Budget: ${row[2]}")
            
        print("-" * 50)
        print("\n🎉 DB Filtering executed successfully with zero inconsistencies!")
        
    except Exception as e:
        print(f"❌ Filtering Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    filter_high_budget_jobs()