# 🛡️ Sudhir's Master Python Automation Cheat-Sheet

## 1. 🌐 Web Scraping (BeautifulSoup Syntax)
```python
import requests
from bs4 import BeautifulSoup

url = "TARGET_URL"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
# Find singular item
title = soup.find('h1').text.strip()
# Find multiple items (Loop)
items = soup.find_all('p')
for item in items:
    print(item.text.strip())
```

## 2. 🗄️ Database Management (SQLite3 Syntax)
```python
import sqlite3

conn = sqlite3.connect("sudhir_projects.db")
cursor = conn.cursor()

# Parameterized Secure Query (Shield against Injection)
query = "SELECT * FROM upwork_jobs WHERE job_title = ?"
cursor.execute(query, (user_input,))
rows = cursor.fetchall()

conn.commit()
conn.close()
```

## 3. 🔗 Data Structures (Linked List Node Syntax)
```python
class LawyerNode:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.next = None  # Pointer to next memory address
```
