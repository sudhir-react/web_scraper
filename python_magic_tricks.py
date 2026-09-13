def run_sudhir_python_magic():
    print("🚀 Starting Sudhir's Advanced Python Magic Tricks Test...\n")
    
    # ----------------------------------------------------
    # Trick 1: List Comprehension (Filter for budgets above $100 only)
    # ----------------------------------------------------
    all_budgets = [45, 120, 30, 500, 75, 1500]
    # The magic of loops and if-conditions in just one line.
    premium_budgets = [b for b in all_budgets if b > 100]
    print(f"🎯 Trick 1 (Filtered Premium Budgets): {premium_budgets}")
    
    # ----------------------------------------------------
    # Trick 2: Multiple Assignment (Swapping values ​​without a third container)
    # ----------------------------------------------------
    sudhir_rank = "Junior"
    client_rank = "Expert"
    
    # Magical Swapping – Changing ranks in a flash
    sudhir_rank, client_rank = client_rank, sudhir_rank
    print(f"🔒 Trick 2 (Sudhir's New Verified Rank): {sudhir_rank}")
    
    # ----------------------------------------------------
    # Trick 3: The Zip Function (The ultimate union of laptops and prices)
    # ----------------------------------------------------
    laptops = ["MacBook", "Dell XPS", "ThinkPad"]
    prices = [1500, 1200, 800]
    
    print("\n📊 Trick 3 (Zipped Inventory Display):")
    print("-" * 40)
    # zip() processes both lists in parallel.
    for laptop, price in zip(laptops, prices):
        print(f"💻 Laptop: {laptop} | 💰 Price: ${price}")
    print("-" * 40)
    
    print("\n🎉 All 3 Python senior tricks executed with 100% data integrity!")

if __name__ == "__main__":
    run_sudhir_python_magic()