import pandas as pd
import time

def run_multi_page_automation():
    print("🚀 Starting Sudhir's Advanced Multi-Page Scraping Loop...\n")
    
    # 1. जिन अलग-अलग पेजों से डेटा निकालना है, उनकी लिस्ट (Real-world Simulation)
    target_pages = [
        "https://example.com",
        "https://example.com",
        "https://example.com"
    ]
    
    all_extracted_products = []
    
    # 2. MULTI-PAGE LOOP: एक-एक करके हर पेज पर जाना
    for index, url in enumerate(target_pages, start=1):
        print(f"📥 Crawling Target Page #{index}: {url}")
        
        # सीनियर डेवलपर ट्रिक: सर्वर पर इंसानी व्यवहार दिखाने के लिए 2 सेकंड का गैप देना (Anti-Bot Delay)
        time.sleep(2) 
        
        # हर पेज से मिलने वाला सैंपल डेटा (Simulation)
        page_data = [
            {"Product Name": f"Premium Laptop Type-A (Page {index})", "Price": 1200 + (index * 50)},
            {"Product Name": f"Enterprise Storage Drive (Page {index})", "Price": 300 + (index * 20)}
        ]
        
        # डेटा को मुख्य तिजोरी में जोड़ते जाना (.extend)
        all_extracted_products.extend(page_data)
        
    print(f"\n✅ Success: Extracted total {len(all_extracted_products)} records from all pages.")
    
    # 3. पूरे बड़े डेटा को एक ही एक्सेल फ़ाइल में सेव करना
    output_file = "multi_page_inventory.xlsx"
    print(f"💾 Exporting combined dataset directly into '{output_file}'...")
    
    df = pd.DataFrame(all_extracted_products)
    df.to_excel(output_file, index=False)
    
    print(f"\n🎉 Pipeline executed successfully! '{output_file}' is ready for client review.")

if __name__ == "__main__":
    run_multi_page_automation()