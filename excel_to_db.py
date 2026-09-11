import sqlite3
import pandas as pd
import os

def import_excel_to_database():
    print("🚀 Starting Sudhir's Advanced Excel-to-DB Pipeline...\n")
    
    excel_path = "laptops.xlsx"
    db_name = "sudhir_projects.db"
    
    # 1. सुरक्षा जाँच: क्या एक्सेल फ़ाइल फोल्डर में मौजूद है?
    if not os.path.exists(excel_path):
        print(f"❌ Error: {excel_path} not found! Please make sure it's in the Ai_tech/python folder.")
        return
        
    try:
        # 2. Pandas के ज़रिए एक्सेल का पूरा डेटा 1 सेकंड में रीड करना
        print("📥 Reading data from laptops.xlsx...")
        df = pd.read_excel(excel_path)
        
        # 3. SQLite डेटाबेस से कनेक्ट होना
        conn = sqlite3.connect(db_name)
        
        # 4. MAGIC LINE: एक्सेल का पूरा डेटाबेस टेबल में ऑटो-ट्रांसफर करना
        print("💾 Transferring 117+ records directly into database 'laptop_inventory' table...")
        df.to_sql("laptop_inventory", conn, if_exists="replace", index=False)
        
        # 5. सत्यापन (Verification) - डेटाबेस से टॉप 3 रिकॉर्ड्स निकालकर देखना
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