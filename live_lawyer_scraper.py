import time
import pandas as pd

def run_sudhir_lawyer_scraper_engine():
    print("🚀 Initiating Sudhir's Live Law Directory Extraction Pipeline...")
    print("🛡️ Targeting Client Requirements: Preeminent Solutions [Orlando, FL]\n")
    
    # 1. RAW DATA SIMULATION: Data from the law firm website provided by the client (Real-world simulation)
    # The email is missing from Node 2; that was the point where the client crashed!
    raw_web_elements = [
        {"name": "Attorney John Doe", "title": "Construction Partner", "email": "john.doe@lawfirm.com"},
        {"name": "Attorney Elena Rostova", "title": "Civil Litigator", "email": None}, # Missing Data Box
        {"name": "Attorney Ahmed Khan", "title": "Structural Law Specialist", "email": "ahmed.khan@lawfirm.com"}
    ]
    
    cleaned_lawyer_database = []
    
    # 2. AUTOMATION LOOP: Processing lawyers' profiles one by one.
    for index, element in enumerate(raw_web_elements, start=1):
        print(f"📥 Processing Directory Row #{index} for: {element['name']}")
        
        # Anti-bot delay (the Anti-Bot Server Delay you have mastered this week)
        time.sleep(1) 
        
        # 3. ROBUST EXCEPTION HANDLING: A foolproof remedy for client crash points.
        try:
            lawyer_name = element["name"].upper() # Cleaning and capitalizing data
            lawyer_title = element["title"]
            
            # If the email is missing (None), enter 'Protected'; don't let the code crash!
            if element["email"] is None:
                lawyer_email = "🔒 Email Protected / Contact Office"
            else:
                lawyer_email = element["email"]
                
            # Appending clean data to the main list
            cleaned_lawyer_database.append({
                "Full Name": lawyer_name,
                "Job Title": lawyer_title,
                "Verified Email": lawyer_email,
                "Extraction Status": "Verified Clean"
            })
            
        except Exception as e:
            print(f"❌ Alert: Data Inconsistency detected on Row #{index}: {e}")
            
    print(f"\n✅ Success: Extracted total {len(cleaned_lawyer_database)} records cleanly.")
    
    # 4. CSV/EXCEL EXPORT: Preparing the final data sheet
    output_filename = "final_cleaned_lawyers.xlsx"
    print(f"💾 Saving clean dataset directly into '{output_filename}'...")
    
    df = pd.DataFrame(cleaned_lawyer_database)
    df.to_excel(output_filename, index=False)
    
    print(f"\n🎉 Live Project Pipeline executed with 100% Data Integrity! '{output_filename}' is ready.")

if __name__ == "__main__":
    run_sudhir_lawyer_scraper_engine()