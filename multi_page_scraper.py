import pandas as pd
import time

def run_multi_page_automation():
    print("🚀 Starting Sudhir's Advanced Multi-Page Scraping Loop...\n")
    
    # 1. List of the various pages from which data is to be extracted (Real-world Simulation)
    target_pages = [
        "https://example.com",
        "https://example.com",
        "https://example.com"
    ]
    
    all_extracted_products = []
    
    # 2. MULTI-PAGE LOOP: Navigating through each page one by one.
    for index, url in enumerate(target_pages, start=1):
        print(f"📥 Crawling Target Page #{index}: {url}")
        
        # Senior Developer Trick: Introducing a 2-second gap to mimic human behavior on the server (Anti-Bot Delay)
        time.sleep(2) 
        
        # Sample data (simulation) obtained from each page
        page_data = [
            {"Product Name": f"Premium Laptop Type-A (Page {index})", "Price": 1200 + (index * 50)},
            {"Product Name": f"Enterprise Storage Drive (Page {index})", "Price": 300 + (index * 20)}
        ]
        
        # Appending data to the main vault (.extend)
        all_extracted_products.extend(page_data)
        
    print(f"\n✅ Success: Extracted total {len(all_extracted_products)} records from all pages.")
    
    # 3. Saving the entire big dataset into a single Excel file.
    output_file = "multi_page_inventory.xlsx"
    print(f"💾 Exporting combined dataset directly into '{output_file}'...")
    
    df = pd.DataFrame(all_extracted_products)
    df.to_excel(output_file, index=False)
    
    print(f"\n🎉 Pipeline executed successfully! '{output_file}' is ready for client review.")

if __name__ == "__main__":
    run_multi_page_automation()