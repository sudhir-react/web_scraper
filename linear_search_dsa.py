import time

def perform_sudhir_linear_search(inventory_list, target_item):
    print(f"🔍 Analyzing dataset array containing {len(inventory_list)} items...")
    
    # Starting the algorithm: Scanning the boxes one by one (O(N) Time Complexity)
    for index, element in enumerate(inventory_list):
        if element == target_item:
            return index  # Returning the exact position (index) of the item upon finding it.
            
    return -1  #If the item is not found anywhere in the entire list

def run_dsa_session():
    print("🚀 Initiating Sudhir's Advanced Python DSA Session [Day 14]...\n")
    
    # 1. RAW DATA ARRAY: Inventory List (Data Structure)
    corporate_inventory = ["ThinkPad", "Dell XPS", "MacBook Pro", "HP EliteBook", "Asus ZenBook"]
    
    search_target = "MacBook Pro"
    print(f"🎯 Target Element to Locate: '{search_target}'")
    print("-" * 55)
    
    # Starting the timer (for performance audit)
    start_time = time.perf_counter()
    
    # 2. ALGORITHM EXECUTION: Calling the algorithm
    result_index = perform_sudhir_linear_search(corporate_inventory, search_target)
    
    end_time = time.perf_counter()
    execution_duration = (end_time - start_time) * 1000  # time in milliseconds
    
    # 3. OUTPUT UI: Polishing the result
    print("-" * 55)
    if result_index != -1:
        print(f"✅ SUCCESS: Element located perfectly inside Data Structure!")
        print(f"🆔 Found at Array Index Position: {result_index} (Slot #{result_index + 1})")
    else:
        print("❌ CRITICAL: Target element not present in the array architecture.")
        
    print(f"⚡ Algorithm Execution Time: {execution_duration:.4f} ms")
    print(f"📊 Worst-Case Complexity: O(N) - Linear Time Scaling")
    print("\n🎉 Python DSA logic executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_dsa_session()