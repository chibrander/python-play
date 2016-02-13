import requests
import bs4
def newlist():
    page = requests.get("http://www.cybersyndrome.net/pla.html")

    content = bs4.BeautifulSoup(page.content,'html.parser')

    li = content.find("ol").findAll("li")


    proxli = []

    for l in li:
        if l.a['title'] == 'US':
            proxli.append(l.a.string)

    print(proxli)
    print(len(proxli))

    return proxli
