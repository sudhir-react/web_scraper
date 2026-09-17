import time

def find_two_sum_optimized(price_list, target_budget):
    print(f"⚡ Running Hash Map Optimization for target sum: ${target_budget}...")
    
    #this is our magical memory card (Hash Map).
    seen_prices = {}
    
    # Just a single loop (O(N) Time Complexity – super fast)
    for index, current_price in enumerate(price_list):
        required_partner = target_budget - current_price
        
        # Check the memory card to see if the number we need is already there.
        if required_partner in seen_prices:
            return [seen_prices[required_partner], index]
            
        # If it is not there, save the current number along with its position to the memory card.
        seen_prices[current_price] = index
        
    return []

def run_optimized_session():
    print("🚀 Initiating Sudhir's Premium O(N) Algorithm Optimization...\n")
    
    laptop_prices = [400, 900, 1200, 500, 800]
    target_budget = 1700
    
    start_time = time.perf_counter()
    
    # Calling optimized algorithms
    indices = find_two_sum_optimized(laptop_prices, target_budget)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 65)
    if indices:
        print(f"🎯 OPTIMIZED MATCH FOUND SUCCESSFULY!")
        print(f"🆔 Perfect Array Indices Located: {indices}")
        print(f"💻 Smart Pair: ${laptop_prices[indices[0]]} + ${laptop_prices[indices[1]]} = ${target_budget}")
    else:
        print("❌ Budget requirement pair not found.")
        
    print(f"⚡ Optimized Execution Time: {duration:.4f} ms")
    print(f"📊 Computational Complexity: O(N) - Linear Time Efficiency")
    print("-" * 65)
    print("\n🎉 High-Performance Architecture executed with 100% memory efficiency!")

if __name__ == "__main__":
    run_optimized_session()