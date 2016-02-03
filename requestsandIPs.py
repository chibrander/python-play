import requests
import pickle
from bs4 import BeautifulSoup

def makep(url):
    proxies = {
    #"http": "http://211.137.39.61:8080",
    "http": "111.14.40.155:81",
    }
    headers = {'user-agent': '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    try:
        r = requests.get(url,headers=headers,timeout=10, proxies=proxies)
        print(r.status_code)
        print(r.status_code == requests.codes.ok)
        pf = open("data","wb")
        pickle.dump(r.content,pf)
        pf.close()
        pcf = open("cookie","wb")
        pickle.dump(r.cookies,pcf)
        pcf.close()
    except:
        print("There Was a Problem")

def readp(name):
    opf = open(name, "rb")
    html = pickle.load(opf,encoding="UTF-8")
    html = html.decode("UTF-8")
    print(html)
    opf.close()

def readr(name):
    opf = open(name, "rb")
    html = pickle.load(opf,encoding="UTF-8")
    html = html.decode("UTF-8")
    return html
    opf.close()


def get_tables(htmldoc):
    soup = BeautifulSoup(htmldoc,'html.parser')
    tables =  soup.findAll('table')
    return tables[0].findAll('tr')


def getips():
    makep('http://www.samair.ru/proxy-by-country/China-01.htm')
    t = get_tables(readr("data"))
    arr = []
    for p in t:
        arr.append(p.td.string)
    return arr

#makep('http://whatismyipaddress.com/')
#makep('http://www.samair.ru/proxy-by-country/China-01.htm')

mr = getips()


print(mr)
