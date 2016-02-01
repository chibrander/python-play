import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

class bay:
    def make(x,kw):

        try:
            url = 'http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Complete=1&LH_Sold=1&LH_ItemCondition=3&_nkw=' + kw + '&_pgn=' + str(x) + '&_ipg=200&rt=nc'
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers = headers)
            response = urllib.request.urlopen(req)
            html = response.read()
            f = open("page.html","w")
            f.write(str(html))
            f.close()
            print("File Made!")

        except Exception as e:
            print(str(e))


    def get(n,fn):
        ht = open("page.html","r")
        html_doc = ht.read()
        html_doc = html_doc.replace("\\n","")
        html_doc = html_doc.replace("\\r","")
        html_doc = html_doc.replace("\\t","")
        soup = BeautifulSoup(html_doc, 'html.parser')
        titles = soup.find_all(class_="lvtitle")

        titlearray = []
        for title in titles:
            titlearray.append(title.a.string)


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


        prices = soup.find_all(class_="bold bidsold")

        pricearray = []
        for price in prices:
            pr = price.string
            try:
                p = re.search('[\d.,]+', pr)
                prc = p.group(0)
            except:
                prc = "NaN"
            pricearray.append(prc)

        df1 = pd.DataFrame(data = titlearray, columns=['Titles'])
        df2 = pd.DataFrame(data = pricearray, columns=['Price'])
        df3 = pd.DataFrame(data = datearray, columns=['Date'])
        df4 = pd.DataFrame(data = imagearray, columns=['Image'])
        df1['Prices'] = df2
        df1['Dates'] = df3
        df1['Image'] = df4
        df1.to_excel(fn + str(n) + '.xlsx', index=False)
        print('Created: ' + fn + str(n) + '.xlsx')
