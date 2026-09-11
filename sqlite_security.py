import sqlite3

def run_database_security_test():
    print("🛡️ Starting Sudhir's Advanced DB Security & Integrity Test...\n")
    
    db_name = "sudhir_projects.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        # 1. Creating a new table with a safety constraint (UNIQUE constraint)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS secure_inventory (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL UNIQUE,
                price REAL
            )
        ''')
        print("✅ Step 1: Secure table with UNIQUE protection is ready.")
        
        # 2.Inserting the correct data the first time
        print("📥 Step 2: Inserting 'Scale Plan' for the first time...")
        cursor.execute("INSERT INTO secure_inventory (item_name, price) VALUES ('Scale Plan', 150.0)")
        conn.commit()
        print("👍 Success: First record saved smoothly.")
        
        # 3. DANGER ZONE: Deliberately attempting to enter the same name again (test to prevent data clutter)
        print("\n⚠️ Step 3: Attempting to insert duplicate 'Scale Plan' to test security...")
        cursor.execute("INSERT INTO secure_inventory (item_name, price) VALUES ('Scale Plan', 150.0)")
        conn.commit()
        
    except sqlite3.IntegrityError as e:
        # If the safety net works, Python will catch this error itself!
        print("\n🔒 DATABASE SECURITY ALERT TRIGGERED SUCCESSFULY!")
        print(f"🛑 Integrity Shield blocked the duplicate entry: {e}")
        print("🎯 Reason: Sudhir's UNIQUE constraint prevented database corruption.")
        
    except Exception as general_error:
        print(f"❌ Other Error: {general_error}")
        
    finally:
        # Viewing the current status from the database
        cursor.execute("SELECT * FROM secure_inventory")
        records = cursor.fetchall()
        print("\n📊 Current Clean Database Records:")
        print("-" * 40)
        for row in records:
            print(f"🆔 ID: {row[0]} | 💻 Name: {row[1]} | 💰 Price: ${row[2]}")
        print("-" * 40)
        
        conn.close()
        print("\n🎉 Security Architecture execution completed successfully!")

if __name__ == "__main__":
    run_database_security_test()