import requests
from bs4 import BeautifulSoup

keyworld = "파이썬"
pages = 5

for page in range(pages):
    page = page * 30
    url = f'https://search.incruit.com/list/search.asp?col=job&kw=파이썬{keyworld}startno={page}'
    r= requests.get(url)
    #print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    print(f"{i+1}")


  

    print(soup.prettify)

    lis = soup.find_all("li", class_="c_col")
    print(lis)

    for li in lis:
        try:
            company = li.find("a", class_="cpname").text
            title = li.find("div", class_="cell_mid").find("a").text
            location = li.find("div", class_="cl_md").find_all("span")[0].text
            title = li.find("div", class_="cell_mid").find("a").get("href")
            link = li.find("dev", class_="cell_mid"),find("a").get("href")


    job_data = {
        "company": company
        "title": title,
        "location": location,
        "link": link
    }        

    jobs.appennd(job_data)

    print(location)
        except:
            pass

print(jobs)

for i in range(pages):


