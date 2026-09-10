import requests
from bs4 import BeautifulSoup
import pandas as pd

def run_excel_automation():
    print("🚀 Sudhir's Excel Automation Script is starting...\n")
    
    url = "https://webscraper.io"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # 1. Scraping data from a live website
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        product_titles = soup.find_all("a", class_="title")
        if len(product_titles) == 0:
            product_titles = [card.find('a') for card in soup.find_all('h4') if card.find('a')]

        print(f"🎯 Total {len(product_titles)} laptops detected from the live website.")
        
        # 2.Creating an empty list to organize data 
        laptop_list = []
        serial_no = 1
        
        # 3.Formatting the data entirely in English using a for loop.
        for product in product_titles:
            name = product.text.strip()
            if name:
                # Adding every laptop to the list along with its serial number.
                laptop_list.append({
                    "Serial No.": serial_no,
                    "Laptop Name": name
                })
                serial_no += 1

        # 4. The Magic of Pandas: Converting Data into a DataFrame (Table)
        df = pd.DataFrame(laptop_list)
        
        # 5.EXCEL AUTOMATION: Saving data to the 'laptops.xlsx' file on the laptop.
        excel_filename = "laptops.xlsx"
        df.to_excel(excel_filename, index=False)
        
        print(f"\n🎉 Congratulations Sudhir Mishra! File '{excel_filename}' created successfully!")
        print("➡️ Check your python folder, your brand new Excel Sheet is waiting for you.")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    run_excel_automation()