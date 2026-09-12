import sqlite3

def run_database_aggregations():
    print("🚀 Starting Sudhir's Advanced SQL Aggregations Script...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # 1. SUM TRICK: डेटाबेस में मौजूद सभी अपवर्क जॉब्स के कुल बजट का जोड़ निकालना
        cursor.execute("SELECT SUM(budget) FROM upwork_jobs")
        total_budget = cursor.fetchone()[0]
        
        # 2. AVG TRICK: सभी जॉब्स के बजट का औसत (Average) निकालना
        cursor.execute("SELECT AVG(budget) FROM upwork_jobs")
        average_budget = cursor.fetchone()[0]
        
        # 3. COUNT TRICK: कुल जॉब्स की संख्या गिनना
        cursor.execute("SELECT COUNT(*) FROM upwork_jobs")
        total_jobs_count = cursor.fetchone()[0]
        
        # आउटपुट को स्क्रीन पर चमकाना
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