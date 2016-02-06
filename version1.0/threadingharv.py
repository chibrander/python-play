import bayclass as e
import time
import random
from threading import Thread


def rotate(lst,shiftnumber):
    return lst[shiftnumber:len(lst)] + lst[0:shiftnumber]

me = []
# Set Initial Proxy to Get New Proxies

for n in range(1,5):
    me.append(e.Bay("40.76.53.46:80"))


me[0].getips()


plist = me[0].proxies
print(plist)

lnum = 0
for obj in me:
    obj.proxies = rotate(plist,lnum)
    lnum = lnum + 7

for i in me:
    print(i.proxies)




def miltiharv(obj,kw,fn):
    for i in reversed(range(1,50)):
        n = int(random.random()*100)+1+50
        obj.set(i,kw)
        time.sleep(3)
        obj.get(i,fn)
        time.sleep(n)

#print(me.gethtml("data.ht"))

def start():
    trd = []
    kws = ["lingerie+plus","lingerie+women","lingerie","sexy+lingerie"]
    i = 0
    for obj in me:
        trd.append(Thread(target=miltiharv,args=(obj,kws[i],kws[i].replace("+",""))))
        i = i + 1

    for tr in trd:
        tr.start()

start()
