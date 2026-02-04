import os
from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient

# 1. Load your API key from the .env file
load_dotenv()
api_key = os.getenv("SCRAPING_API_KEY")

# 2. Initialize the client
client = ScrapingBeeClient(api_key=api_key)

# 3. Define the URL you want to scrape
target_url = "https://www.techcrunch.com"

print(f"Scraping {target_url} using ScrapingBee...")

# 4. Make the request
# Note: 'render_js': True tells ScrapingBee to use a real browser (Selenium-style)
response = client.get(
    target_url,
    params={
        'render_js': 'True',
    }
)

if response.ok:
    print('Success!')
    print('Response HTTP Status Code: ', response.status_code)
    # response.content gives you the raw HTML
    print('First 500 characters of HTML:', response.text[:500])
else:
    print('Something went wrong.')
    print(response.content)