import requests
from bs4 import BeautifulSoup

def web_crawler(url, depth=2, max_recursions=6):
    result_list = []

    def crawl(url, current_depth, recursion_count):
        if current_depth > depth or recursion_count > max_recursions:
            print(f"Crawling: {url}")
            return

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                page_info = {
                    'url': url,
                    'title': soup.title.text if soup.title else '',
                    'text': soup.get_text()
                }

                result_list.append(page_info)

                links = soup.find_all('a', href=True)
                """ Inside the loop over the links on the page, the function makes a recursive call 
                                        (crawl(next_url, current_depth + 1, recursion_count + 1)) 
                                        with an incremented recursion_count."""
                for link in links:
                    next_url = link['href']

                    if next_url.startswith('http'):
                        """the recursion_count is crucial in controlling the depth of recursion and avoiding an infinite loop 
                        or exceeding the maximum recursion limit"""
                        crawl(next_url, current_depth + 1, recursion_count + 1)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    crawl(url, 1, 0)  # Start with recursion_count as 0
    return result_list

# Example usage:
result = web_crawler("https://example.com", depth=2, max_recursions=5)
print(result)
