import requests
from bs4 import BeautifulSoup

keyworld = "파이썬"
url = f'https://search.incruit.com/list/search.asp?col=job&kw=파이썬{keyworld}'
r= requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify)

lis = soup.find_all("li", class_="c_col")
print(lis)

for li in lis:
    try:
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("a").text
        location = li.find("div", class_="cl_md").find_all("span")[0].text
        title = li.find("div", class_="cell_mid").find("a").get("href")
        print(location)
    except:
        pass
