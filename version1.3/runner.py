import bayclass as e
import time
import random
from threading import Thread
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import math

# set variables
firstproxyer = '104.236.220.70:80'

words = ["one size thong","one size yoga pants","one size panties","one size socks","one size g string","one size leggings"]
keywords_per_run = 2

dr = 'Excel'
proxyshift = 7
lastpage = 40

uname = 'luggag5_pr'
upass = 'pass'
uhost= '205.134.250.36'
udb = 'luggag5_pr'

# set variables END


sql_alch_con = 'mysql+pymysql://' + uname + ':' + upass + '@' + uhost + '/' + udb + '?charset=utf8'


runcount = len(words) / keywords_per_run
runcount = math.ceil(runcount)+1

prx = e.Bay(firstproxyer)
prx.getips()
print(prx.proxies)


def ipget():
    if len(prx.proxies) >0:
        if prx.getips():
           return prx.proxies
        else:
            prx.proxies.pop(0)
            ipget()
    else:
        return e

engine = create_engine(sql_alch_con, echo=False)



# proxyshift function
def rotate(lst,shiftnumber):
    return lst[shiftnumber:len(lst)] + lst[0:shiftnumber]
# proxyshift function END


def initobj(kws,proxyshift,firstproxy,plist):
    # Make a List to Hold All Threading Objects
    me = []

    # Create As Many Objects as Keywords
    for n in range(1,len(kws)+1):
        me.append(e.Bay(firstproxy))
    #
    # # Get a Fresh Proxy List
    # me[0].getips()
    # plist = me[0].proxies
    # print(plist)

    # Rotate Proxies and Assign to Each Object
    lnum = 0
    for obj in me:
        obj.proxies = rotate(plist,lnum)
        lnum = lnum + proxyshift

    for i in me:
        print(i.proxies)

    return me

# Function to Harvest & Write Data with Random Intervals
def miltiharv(obj,kw,fn,dr):
    for i in reversed(range(1,lastpage+1)):
        n = int(random.random()*100)+1+50
        obj.set(i,fn,kw)
        time.sleep(1)
        obj.get(i,fn,dr)
        time.sleep(1)
        dff = pd.read_excel("excel/" + fn + ".xlsx")

        if dff.empty:
            pass
        else:
            try:
                #connection = engine.connect()
                dff = dff.fillna("None")
                print(dff)
                dff.to_sql(name='testproducts', con=engine, if_exists = 'append', index=False)
                #connection.close()
            except Exception as e:
                print(e)
                time.sleep(2)
                try:
                    #connection = engine.connect()
                    dff.to_sql(name='testproducts', con=engine, if_exists = 'append', index=False)
                    #connection.close()
                except Exception as e:
                    print(e)

        time.sleep(n)
#print(me.gethtml("data.ht"))

# Function to Start Harvesting & Writing Over Multiple Threads
def start(me,kws):
    trd = []
    i = 0
    for obj in me:
        trd.append(Thread(target=miltiharv,args=(obj,kws[i].replace(" ","+"),kws[i].replace(" ",""),dr)))
        i = i + 1

    for tr in trd:
        tr.start()

    for tr in trd:
        tr.join()


def kwcount(x,proxyshift):
    for t in range(1,runcount):
        beg = (t-1) * x
        end = beg + x
        kws = words[beg:end]
        freshproxylist = ipget()
        print('Fresh Proxies:')
        print(freshproxylist)
        print("Initiating New Process for This Round...")
        time.sleep(2)
        # Start it All Here
        mefinal = initobj(kws,proxyshift,freshproxylist[0],freshproxylist)
        start(mefinal,kws)

kwcount(keywords_per_run,proxyshift)
