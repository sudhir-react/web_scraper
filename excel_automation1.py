import requests
from bs4 import BeautifulSoup
import pandas as pd

def run_excel_automation():
    print("🚀 Sudhir's Excel Automation Script (Version 2) is starting...\n")
    
    # Link to the live shopping test site
    url = "https://webscraper.io"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 1.Universal Logic: 3 different ways to find laptop names
        product_titles = []
        
        # Method A: Finding all links with the 'title' class
        links = soup.find_all("a", class_="title")
        if links:
            product_titles = [l.text.strip() for l in links]
            
        #Method B: If Method A fails, find links inside 'h4'.
        if len(product_titles) == 0:
            h4_tags = soup.find_all("h4")
            for h4 in h4_tags:
                a_tag = h4.find("a")
                if a_tag:
                    product_titles.append(a_tag.text.strip())
                    
        # Method C: If both fail, pick the raw text of 'h4'.
        if len(product_titles) == 0:
            product_titles = [h4.text.strip() for h4 in soup.find_all("h4") if h4.text.strip()]

        print(f"🎯 Total {len(product_titles)} laptops detected from the live website.")
        
        # 2. Organizing data
        laptop_list = []
        serial_no = 1
        
        for name in product_titles:
            if name and "caption" not in name.lower(): # To remove unnecessary text
                laptop_list.append({
                    "Serial No.": serial_no,
                    "Laptop Name": name
                })
                serial_no += 1

        # 3. Pandas to Excel Automation: Saving to a file
        df = pd.DataFrame(laptop_list)
        excel_filename = "laptops.xlsx"
        df.to_excel(excel_filename, index=False)
        
        print(f"\n🎉 Congratulations Sudhir Mishra! File '{excel_filename}' updated successfully!")
        print("➡️ Open your python folder and double-click 'laptops.xlsx' to see the data!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    run_excel_automation()