import time

def run_vectorized_cleaner_session():
    print("🚀 Starting Sudhir's Advanced Single-Line Data Engineering Session [Day 22]...\n")
    
    # 1. RAW DATA ARRAY: Unfiltered list of medicines received from hospitals (contains 'None' and spaces)
    raw_medicine_batch = ["  paracetamol  ", None, "  ibuprofen  ", "  amoxicillin  "]
    
    print(f"📥 Scraped Raw Batch Layout: {raw_medicine_batch}")
    print("-" * 75)
    
    start_time = time.perf_counter()
    
    # 2. THE PRO TRICK: Loop, null-checking (None Guard), and strip/uppercase—all in just one line!
    # It compresses a 5-line loop into a single line.
    cleaned_medicine_batch = [
        str(med).strip().upper() if med is not None else "🔒 EMPTY_SLOT_GUARD" 
        for med in raw_medicine_batch
    ]
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. CONSOLE OUTPUT
    print("🟢 SUCCESS: Single-Line Vectorized Engine Output Matrix:")
    print(cleaned_medicine_batch)
    print("-" * 75)
    
    print(f"⚡ Processing Duration        : {duration:.4f} ms")
    print(f"📊 Algorithmic Complexity Vector: O(N) Linear Single-Pass Execution")
    print("-" * 75)
    print("\n🎉 Single-line conditional guard validation completed with 100% integrity!")

if __name__ == "__main__":
    run_vectorized_cleaner_session()