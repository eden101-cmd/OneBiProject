import requests
from bs4 import BeautifulSoup

def crawl_page(url, depth=2):
    """
    Crawl a web page and its linked pages up to a specified depth.
    Arg:
        url (str): The starting URL to crawl.
        depth (int): The maximum depth to crawl. Default is 2.
    Returns:
        list: A list of dictionaries containing information about crawled pages.
              Each dictionary has 'url', 'title', and 'text' keys.
    """
    visited_urls = set()

    def extract_text(soup):
        """
        Extract text content from BeautifulSoup soup object.
    Arg:
            soup (BeautifulSoup): The BeautifulSoup object representing a web page.
    Returns:
            str: Extracted text content.
        """
        all_text = ' '.join(element.get_text() for element in soup.find_all(True, recursive=False))
        return all_text.strip()

    def crawl(url, current_depth):
        """
        Recursive function to crawl a web page and its linked pages.
    Arg:
            url (str): The URL of the current page.
            current_depth (int): The current depth of recursion.
    Returns:
            None
        """
        if current_depth > depth or url in visited_urls:
            return

        visited_urls.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url)

            # Check for successful response (status code 200)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                page_info = {
                    'title': soup.title.text if soup.title else '',
                    'url': url,
                    'text': extract_text(soup)
                }

                result_list.append(page_info)

                # Extract links from the current page and recursively crawl them
                links = soup.find_all('a', href=True)
                for link in links:
                    next_url = link['href']
                    if next_url.startswith('http'):
                        crawl(next_url, current_depth + 1)
            else:
                print(f"Error crawling {url}: HTTP Status Code {response.status_code}")

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    result_list = []
    crawl(url, 1)
    return result_list
