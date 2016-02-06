import bayclass as e
import time
import random
from threading import Thread

# set variables
kws = ["lingerie plus","lingerie women","sexy lingerie"]
dr = 'Excel'
proxyshift = 7
firstproxy = '40.76.53.46:80'
lastpage = 49
# set variables END

# proxyshift function
def rotate(lst,shiftnumber):
    return lst[shiftnumber:len(lst)] + lst[0:shiftnumber]
# proxyshift function END

# Make a List to Hold All Threading Objects
me = []

# Create As Many Objects as Keywords
for n in range(1,len(kws)+1):
    me.append(e.Bay(firstproxy))

# Get a Fresh Proxy List
me[0].getips()
plist = me[0].proxies
print(plist)

# Rotate Proxies and Assign to Each Object
lnum = 0
for obj in me:
    obj.proxies = rotate(plist,lnum)
    lnum = lnum + proxyshift

for i in me:
    print(i.proxies)

# Function to Harvest & Write Data with Random Intervals
def miltiharv(obj,kw,fn,dr):
    for i in reversed(range(1,lastpage+1)):
        n = int(random.random()*100)+1+50
        obj.set(i,kw)
        time.sleep(3)
        obj.get(i,fn,dr)
        time.sleep(n)

#print(me.gethtml("data.ht"))

# Function to Start Harvesting & Writing Over Multiple Threads
def start():
    trd = []
    i = 0
    for obj in me:
        trd.append(Thread(target=miltiharv,args=(obj,kws[i].replace(" ","+"),kws[i].replace(" ",""),dr)))
        i = i + 1

    for tr in trd:
        tr.start()

# Start it All Here
start()
