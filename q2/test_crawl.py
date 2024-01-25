import queue
from pathlib import Path
import requests
from bs4 import BeautifulSoup

def crawl(base_url, start_anchor):
    search_anchors = queue.Queue()
    urls = []
    while True:
        if not start_anchor:
            start_anchor = '/'
        response = requests.get(base_url + start_anchor)  # Fixed: use requests.get
        soup = BeautifulSoup(response.text, "lxml")
        anchors = find_local_anchors(soup, start_anchor)
        if anchors:
            for a in anchors:
                url = base_url + a
                if url in urls:
                    continue
                if not Path(a).suffix:
                    search_anchors.put(a)
                urls.append(url)
        if search_anchors.empty():
            break
        start_anchor = search_anchors.get()
    return urls

def find_local_anchors(soup, start_anchor):
    anchors = []
    for link in soup.find_all('a'):
        anchor = link.get("href", '')  # Fixed: use link.get to avoid potential KeyError
        if anchor.startswith(start_anchor):
            anchors.append(anchor)
    return anchors

