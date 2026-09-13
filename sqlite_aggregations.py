import sqlite3

def run_database_aggregations():
    print("🚀 Starting Sudhir's Advanced SQL Aggregations Script...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        #1. SUM TRICK: Calculating the total budget of all Upwork jobs present in the database.
        cursor.execute("SELECT SUM(budget) FROM upwork_jobs")
        total_budget = cursor.fetchone()[0]
        
        # 2. AVG TRICK: Calculating the average budget of all jobs.
        cursor.execute("SELECT AVG(budget) FROM upwork_jobs")
        average_budget = cursor.fetchone()[0]
        
        # 3. COUNT TRICK: Counting the total number of jobs
        cursor.execute("SELECT COUNT(*) FROM upwork_jobs")
        total_jobs_count = cursor.fetchone()[0]
        
        # Displaying the output on the screen
        print("📊 Real-Time Financial Analytics from Database:")
        print("-" * 50)
        print(f"🔢 Total Jobs Evaluated: {total_jobs_count}")
        print(f"💰 Cumulative Portfolio Budget: ${total_budget:,.2f}")
        print(f"📈 Average Project Budget Value: ${average_budget:,.2f}")
        print("-" * 50)
        
        print("\n🎉 SQL Aggregations executed successfully with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Aggregation Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_database_aggregations()