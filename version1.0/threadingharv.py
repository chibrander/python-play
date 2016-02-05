import bayclass as e
import time
import random
from threading import Thread

# Set Initial Proxy to Get New Proxies
me = e.Bay("111.14.40.155:8081")

# Get New Proxies
me.getips()
print(me.proxies)

me2 = e.Bay("111.14.40.155:8081")

# Get New Proxies
me2.getips()
print(me2.proxies)


# Or Use Your Own Proxies
proxz = me.proxies
proxz = list(reversed(proxz))

me.proxies = proxz

print(me.proxies)



def miltiharv(obj,kw,fn):
    for i in reversed(range(1,50)):
        n = int(random.random()*100)+1+50
        obj.set(i,kw)
        time.sleep(3)
        obj.get(i,fn)
        time.sleep(n)

#print(me.gethtml("data.ht"))

def start():
    trd1 = Thread(target=miltiharv,args=(me,"lingerie+plus","lingerieplus"))
    trd2 = Thread(target=miltiharv,args=(me2,"lingerie+women","lingeriewomen"))
    trd1.start()
    trd2.start()

start()
