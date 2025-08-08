# news-fetch
This Python script automatically scrapes top news headlines from a public news website and saves them to a .txt file.
It uses Requests to fetch the HTML and BeautifulSoup to parse the webpage and extract headlines.

⚙️ Tools & Libraries
Python 3

requests – to send HTTP requests and fetch webpage content

BeautifulSoup (bs4) – to parse HTML and extract data

📂 Files
news_scraper.py → Python script to run the scraper

headlines.txt → Output file containing scraped news headlines

How to Run
Install required libraries
pip install requests beautifulsoup4
Run the script

python news_scraper.py
Check the output
Open headlines.txt to see the saved news headlines.
