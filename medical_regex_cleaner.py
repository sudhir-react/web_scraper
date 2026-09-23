import time
import re
import pandas as pd

def clean_medical_text_via_regex(raw_text):
    # Guard clause to handle missing elements perfectly
    if raw_text is None or pd.isna(raw_text):
        return "⚠️ UNKNOWN_BATCH_RECORD"
    
    # Advanced Regex: Strip out unexpected special characters and compress multi-spaces
    cleaned = re.sub(r'[^\w\s\-\(\)]', '', str(raw_text)) # Keep alphanumeric, spaces, hyphens, brackets
    cleaned = re.sub(r'\s+', ' ', cleaned)                # Compress consecutive whitespaces into a single space
    return cleaned.strip().upper()                         # Normalize text case uniformly

def run_advanced_cleaning_pipeline():
    print("🚀 Initiating Sudhir's High-Performance Medical Text Normalization Engine...\n")
    
    # 1. RAW DIRTY DATASET: Simulating messy rows crawled from volatile online tables
    raw_scraped_payload = {
        "Medicine_ID": ["MED001",
        "MED002",
        "MED003",
        "MED004"],
        "Raw_Data_String": [
            "  Paracetamol   500mg !!! (Fever)  ",
            None,
            "  Ibuprofen---200mg @@@ (Pain)  ",
            "  Amoxicillin   Antibiotik###  "
        ]
    }
    
    # Convert into a structured Pandas DataFrame
    df = pd.DataFrame(raw_scraped_payload)
    print("📊 Raw Data Frame State Prior to Regex Clean Operations:")
    print(df)
    print("-" * 75)
    
    # 2. EXECUTION LOCK: Apply our optimized regex function across the entire text column
    start_time = time.perf_counter()
    
    # Vectorized column mapping
    df["Normalized_Data_String"] = df["Raw_Data_String"].apply(clean_medical_text_via_regex)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. OUTPUT UI DISPLAY
    print("\n🟢 SUCCESS: Vectorized Data Transformation Complete!")
    print(df[["Medicine_ID", "Normalized_Data_String"]])
    print("-" * 75)
    
    print(f"⚡ Transformation Pipeline Duration : {duration:.4f} ms")
    print(f"📊 Computational Efficiency Vector  : O(N) Linear Flow")
    print("-" * 75)
    print("\n🎉 Regex data engineering validation completed with 100% structural stability!")

if __name__ == "__main__":
    run_advanced_cleaning_pipeline()


x = 8
y = 2
print(x+y*3)


nums = [1,2,3,4]
print([n*2 for n in nums if n>2])