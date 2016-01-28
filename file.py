import urllib.request
from bs4 import BeautifulSoup


def makeafile():
    #response =  urllib.request.urlopen('http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Complete=1&LH_Sold=1&_nkw=sexy+one+size&rt=nc')
    response =  urllib.request.urlopen('http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Complete=1&LH_Sold=1&_nkw=sexy+one+size&_ipg=200&rt=nc')
    html = response.read()
    f = open("page.html","w")
    f.write(str(html))
    f.close()
    print("File Made!")

#makeafile()

def getstuff():
    ht = open("page.html","r")
    html_doc = ht.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    titles = soup.find_all(class_="lvtitle")
    print(len(titles))
    for title in titles:
        print(title.a.string)



getstuff()
