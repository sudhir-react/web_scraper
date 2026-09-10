import requests
from bs4 import BeautifulSoup

def run_my_first_scraper():
    print("🚀 Sudhir-ji's Python scraping script is starting....\n")
    
    # 1. A link to a live dummy shopping site (website on the internet)
    url = "https://webscraper.io"
    
    # 2.Downloading the entire code of a website by sending a request to it.
    try:
        response = requests.get(url)
        
        # 3. Making code readable with the help of BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 4. Logic: Find the names of all laptops from the website ('a' tags with class="title")
        product_titles = soup.find_all("a", class_="title")
        
        print(f"🎯 Total {len(product_titles)} Data from the laptops was recovered.:\n")
        
        # 5. Printing all the names on the screen using the for loop you learned.
        count = 1
        for product in product_titles[:5]:  #To show only the first 5 laptops
            print(f"💻 laptops {count}: {product.text.strip()}")
            count += 1
            
        print("\n🎉Web scraping completed successfully.!")
        
    except Exception as e:
        print(f"❌ An error occurred: {e} (Please check whether your internet is on or not.)")

if __name__ == "__main__":
    run_my_first_scraper()