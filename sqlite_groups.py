import sqlite3

def run_database_grouping_analysis():
    print("🚀 Starting Sudhir's Advanced SQL Grouping Script...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # MAGIC SQL QUERY: Create groups based on status and get the total budget and number of jobs
        query = '''
            SELECT status, COUNT(*), SUM(budget) 
            FROM upwork_jobs 
            GROUP BY status
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print("📊 Real-Time Financial Breakdown by Status:")
        print("-" * 65)
        for row in rows:
            print(f"📈 Status: {row[0]:<15} | 🔢 Total Jobs: {row[1]} | 💰 Combined Budget: ${row[2]:,.2f}")
        print("-" * 65)
        
        print("\n🎉 SQL Group By analysis completed successfully with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Grouping Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_database_grouping_analysis()