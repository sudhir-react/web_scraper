import requests
from bs4 import BeautifulSoup

def run_my_updated_scraper():
    print("🚀Sudhir-ji's Python scraping script (Version 2) is starting....\n")
    
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    
    #Anti-blocking header (so the website thinks a real human is viewing it via the Chrome browser)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (INTRADAY)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # New and robust logic: Directly locating the 'a' tag or the element with class 'title' inside the 'h4' tag.
        # This approach extracts data in every situation.
        product_titles = soup.find_all("a", class_="title")
        
        # If the old class is not found, we search directly inside the h4.
        if len(product_titles) == 0:
            product_titles = [card.find('a') for card in soup.find_all('h4') if card.find('a')]

        print(f"🎯 total {len(product_titles)} Live data from the laptops was obtained.:\n")
        
        count = 1
        for product in product_titles[:5]:  # To showcase only the first 5 live laptops.
            name = product.text.strip()
            if name:
                print(f"💻 laptop {count}: {name}")
                count += 1
            
        print("\n🎉Congratulations, Sudhir-ji! Web scraping successfully completed.")
        
    except Exception as e:
        print(f"❌ An error occurred.: {e}")

if __name__ == "__main__":
    run_my_updated_scraper()