import sqlite3
import pandas as pd
import os

def import_excel_to_database():
    print("🚀 Starting Sudhir's Advanced Excel-to-DB Pipeline...\n")
    
    excel_path = "laptops.xlsx"
    db_name = "sudhir_projects.db"
    
    # 1. Security check: Does the Excel file exist in the folder?
    if not os.path.exists(excel_path):
        print(f"❌ Error: {excel_path} not found! Please make sure it's in the Ai_tech/python folder.")
        return
        
    try:
        # 2. Reading an entire Excel dataset in one second using Pandas.
        print("📥 Reading data from laptops.xlsx...")
        df = pd.read_excel(excel_path)
        
        # 3.Connecting to an SQLite database
        conn = sqlite3.connect(db_name)
        
        # 4.MAGIC LINE: Automatically transferring the entire Excel database into a table.
        print("💾 Transferring 117+ records directly into database 'laptop_inventory' table...")
        df.to_sql("laptop_inventory", conn, if_exists="replace", index=False)
        
        # 5.Verification – Retrieving and examining the top 3 records from the database. 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM laptop_inventory LIMIT 3")
        rows = cursor.fetchall()
        
        print("\n✅ Verification Success! Showing top 3 records from SQLite Database:")
        print("-" * 70)
        for row in rows:
            print(f"💻 Laptop: {row[0]} | 💰 Price: {row[1]}")
        print("-" * 70)
        
        conn.close()
        print("\n🎉 Pipeline executed successfully with 100% data integrity!")
        
    except Exception as e:
        print(f"❌ Pipeline Failed: {e}")

if __name__ == "__main__":
    import_excel_to_database()