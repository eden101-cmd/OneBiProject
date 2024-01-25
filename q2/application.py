from test_crawl import crawl
from creating_excel_file import making_excel_form,create_excel
def making_url_excel(url,start_anchor):
    urls = crawl(url, start_anchor)
    data = making_excel_form(urls)
    file = create_excel(data)
    return file

making_url_excel("https://www.mit.edu/",start_anchor = "/")