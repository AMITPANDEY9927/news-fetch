import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news website (Example: BBC News)
url = "https://www.bbc.com/news"

# Step 2: Fetch HTML content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 3: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines (BBC uses <h2> tags for titles)
headlines = soup.find_all("h2")

# Step 5: Write headlines to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text:  # Avoid empty lines
            file.write(text + "\n")

print(f"✅ {len(headlines)} headlines saved to headlines.txt")


