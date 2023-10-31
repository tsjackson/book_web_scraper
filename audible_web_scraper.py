import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define the URL of the web page you want to scrape
url: str = 'https://www.audible.com/series/The-Primal-Hunter-Audiobooks/B09MZKWFTB'

# Configure the Chrome WebDriver options for a headless browser
options = Options()
options.add_argument('--headless')  # Run the browser in headless mode (no GUI)
options.add_argument('--window-size=1920x1080')  # Set the window size

# Create a Chrome WebDriver instance
with webdriver.Chrome(options=options) as browser:
    try:
        # Access the specified URL
        browser.get(url)
        page_source = browser.page_source

        # Parse the page source using BeautifulSoup
        soup = BeautifulSoup(page_source, 'lxml')

        # Extract text content from the parsed HTML
        text : str = soup.get_text()

        # Clean up the text: remove newlines and replace multiple spaces with a single space
        text = text.replace('\n', '')
        text = re.sub(r'\s+', ' ', text)

        # Use regular expressions to find series titles (e.g., 'Primal Hunter 1')
        results : list = re.findall(r'(Primal Hunter \d+)', text)

        # Add the first book in the series to the results list
        results.append('Primal Hunter')

        # Remove duplicates by converting the list to a set and back to a list
        unique_results : list = list(set(results))

        # Sort the unique series titles alphabetically
        sorted_results : list = sorted(unique_results)

        # Print the sorted series titles
        print(sorted_results)

    except Exception as e:
        print("Error\n\n", e)