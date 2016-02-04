import requests
import pickle
from bs4 import BeautifulSoup
import pandas as pd
import re
from ipwhois import IPWhois
from ipwhois.utils import get_countries
import time

class Bay:
    def __init__(self,initial_proxy):
            self.proxy = initial_proxy
            self.proxies = []

    def getfile(self,url,proxy,ext=""):
        proxies = {
        #"http": "http://211.137.39.61:8080",
        "http": proxy,
        }
        headers = {'user-agent': '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
        try:
            r = requests.get(url,headers=headers,timeout=10, proxies=proxies)
            print(r.status_code)
            if r.status_code == requests.codes.ok:
                pf = open("data" + ext,"wb")
                pickle.dump(r.content,pf)
                pf.close()
                pcf = open("cookie","wb")
                pickle.dump(r.cookies,pcf)
                pcf.close()
            else:
                return "error"
        except:
            return "error"


    def gethtml(self,name):
        opf = open(name, "rb")
        html = pickle.load(opf,encoding="UTF-8")
        html = html.decode("UTF-8")
        opf.close()
        return html


    def get_tables(self,htmldoc):
        soup = BeautifulSoup(htmldoc,'html.parser')
        tables =  soup.findAll('table')
        return tables[0].findAll('tr')


    def getips(self):
        #ipurl = 'http://www.samair.ru/proxy-by-country/China-01.htm'
        #ipurl = 'https://www.us-proxy.org/'
        ipurl = 'http://www.samair.ru/proxy-by-country/United-States-01.htm'
        self.getfile(ipurl,self.proxy)
        t = self.get_tables(self.gethtml("data"))
        arr = []
        for p in t:
            arr.append(p.td.string)
        self.proxies = arr
        return arr


    def set(self,pagenum,kw):
        try:
            url = 'http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Complete=1&LH_Sold=1&LH_ItemCondition=3&_nkw=' + kw + '&_pgn=' + str(pagenum) + '&_ipg=200&rt=nc'
            if len(self.proxies) > 0:
                countries = get_countries()
                obj = IPWhois(self.proxies[0].split(':')[0])
                results = obj.lookup(False)

                if countries[results['nets'][0]['country']] == "United States":

                    if self.getfile(url,self.proxies[0],".ht") == "error":
                        print("Switching Proxy")
                        self.proxies.pop(0)
                        self.set(pagenum,kw)

                else:
                    print(countries[results['nets'][0]['country']])
                    print("Non-US IP " + self.proxies[0].split(':')[0]  + ": Switching Proxy")
                    self.proxies.pop(0)
                    self.set(pagenum,kw)

            else:
                print("No Proxies in Queue")


        except Exception as e:
            print(str(e))



    def get(self,n,fn):
        html_doc = self.gethtml("data.ht")
        html_doc = html_doc.replace("\n","")
        html_doc = html_doc.replace("\r","")
        html_doc = html_doc.replace("\t","")
        soup = BeautifulSoup(html_doc, 'html.parser')
        listings = soup.find_all(class_="lvresult")
        #titles = soup.find_all(class_="lvtitle")
        #print(listings)
        titlearray = []
        for title in listings:
            titlearray.append(title.find(class_="lvtitle").a.get_text())

        linkarray = []
        for link in listings:
            linkarray.append(link.find(class_="lvtitle").a.get('href'))
        #print(linkarray)


        dates = soup.find_all(class_="tme")
        datearray = []
        for date in dates:
            datearray.append(date.span.string)


        images = soup.find_all(class_="lvpicinner")
        imagearray = []
        for image in images:
            try:
                imagearray.append(image.a.img['imgurl'])
            except:
                try:
                    imagearray.append(image.a.img['src'])
                except:
                    imagearray.append("")


        pricearray = []
        for price in listings:
            pr = price.find(class_="bold bidsold").string
            try:
                p = re.search('[\d.,]+', pr)
                prc = p.group(0)
            except:
                prc = "NaN"
            pricearray.append(prc)


        shippingarray = []
        for shipping in listings:
            try:
                shippingarray.append(shipping.find(class_="bfsp").string)
            except:
                shippingarray.append("None")


        fromarray = []
        for fr in listings:
            try:
                fromarray.append(fr.find(class_="lvdetails").findAll("li")[1].get_text())
            except:
                fromarray.append("")
        #print(fromarray)

        auctionarray = []
        for auction in listings:
            try:
                atext = auction.find(class_="lvformat").get_text()
                if atext == "Buy It Now":
                    auctionarray.append((atext,atext,""))
                else:
                    auctionarray.append((atext[-4:],"Bids",re.search('[\d]+', atext).group(0)))
            except:
                auctionarray.append("")
        #print(auctionarray)



        df1 = pd.DataFrame(data = titlearray, columns=['Titles'])
        df2 = pd.DataFrame(data = pricearray, columns=['Price'])
        df3 = pd.DataFrame(data = datearray, columns=['Date'])
        df4 = pd.DataFrame(data = imagearray, columns=['Image'])
        df5 = pd.DataFrame(data = shippingarray, columns=['Shipping'])
        df6 = pd.DataFrame(data = fromarray, columns=['From'])
        df7 = pd.DataFrame(data = auctionarray, columns=['Auction','Bids','Bids Text'])
        df8 = pd.DataFrame(data = linkarray, columns=['Link'])

        df1['Prices'] = df2
        df1['Dates'] = df3
        df1['Image'] = df4
        df1['Shipping'] = df5
        df1['From'] = df6
        df1[['Auction','Bids','Bids Text']] = df7
        df1['Link'] = df8

        df1.to_excel(fn + str(n) + '.xlsx', index=False)
        print('Created: ' + fn + str(n) + '.xlsx')



# Set Initial Proxy to Get New Proxies
me = Bay("111.14.40.155:8081")

# Get New Proxies
#me.getips()
#print(me.proxies)

# Or Use Your Own Proxies
me.proxies = ['52.27.149.22:80','161.68.250.139:80','161.68.250.181:8080']


me.set(3,'sexy+one+size')
time.sleep(3)
me.get(3,'tst')
