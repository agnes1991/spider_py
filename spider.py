from bs4 import BeautifulSoup
import requests

url = 'https://www.oschina.net/blog'
headers = {
    "content_type":"text/html; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
}


blog_data = requests.get(url, headers=headers)
soup = BeautifulSoup(blog_data.text, 'lxml')

blog_titles = soup.select(".blog-list .item")

for title in blog_titles:
    # for name in blog_name:
    link = title.select(".blog-title-link")
    name = title.select(".blog-name")
    brief = title.select(".blog-brief")
    print(link[0].attrs["href"], name[0].text, "=========", brief[0].text, "\n")

