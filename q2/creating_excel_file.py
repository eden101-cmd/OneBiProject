import pandas as pd
from extractdetails import extract_page_info
from test_crawl import crawl
def create_excel(data):
    df = pd.DataFrame(data, columns=['Page Name', 'URL', 'Page Context'])
    df.to_excel('output.xlsx', index=False)
    print('Excel file created successfully.')

# Example data (replace this with your actual data)

url = "https://www.mit.edu/" # url for example
start_anchor = "/"
urls = crawl(url, start_anchor)


def making_excel_form(urls):
    data = []
    for url in urls:
        try:
            page_info = extract_page_info(url)

            if page_info:
                # Extract relevant information
                page_name = page_info.get('Page Name', 'N/A')
                page_context = page_info.get('Page Context', 'N/A')

                # Create a list with three variables
                entry = url, page_name, page_context

                # Append the list to the data list
                data.append(entry)
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")

    return data


