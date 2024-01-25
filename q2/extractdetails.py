import requests
from bs4 import BeautifulSoup

def extract_page_info(url):
    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        page_name = soup.title.text.strip()

        # Extract the context of the page from various elements (p, div, span)
        page_context_elements = soup.find_all(['p', 'div', 'span'], {'class': True})
        page_context = ' '.join(element.get_text(strip=True) for element in page_context_elements)

        return {'Page Name': page_name, 'Page Context': page_context}

    except Exception as e:
        print(f"Error extracting information from {url}: {e}")
        return None









