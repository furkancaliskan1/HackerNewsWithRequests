import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/"
found_links = []
print("""
    TOP 30 NEWS FROM HACKERNEWS !!!
""")
def get_html(url):
    response = requests.get(url)
    return response


def get_news(url):
    page = get_html(url)
    soup = BeautifulSoup(page.text,features='html.parser')
    i = 0
    for link in soup.find_all('a'):
        found_link = link.get('href')
        if found_link not in found_links:
            if "https://" in found_link and "ycombinator" not in found_link:
                found_links.append(found_link)
                i+=1
                print(str(i)+" >>> "+found_link)


get_news(url)