import bayclass as e
import time
import random
from threading import Thread

# Set Initial Proxy to Get New Proxies
me = e.Bay("111.14.40.155:8081")

# Get New Proxies
#me.getips()
#print(me.proxies)

me2 = e.Bay("111.14.40.155:8081")

# Get New Proxies
me2.getips()
print(me2.proxies)


# Or Use Your Own Proxies

proxz = ['161.68.250.181:8080', '96.5.28.23:8008', '139.162.54.48:8080', '161.68.250.213:80', '173.0.156.203:3128', '161.68.250.167:80', '161.68.250.139:80', '192.241.181.108:8080', '161.68.250.215:80', '161.68.250.185:80', '52.91.193.123:3128', '69.39.30.98:8080', '162.243.49.51:80', '52.35.36.180:80', '52.3.133.160:8080', '161.68.250.143:80', '104.236.49.154:8080', '52.10.100.165:80', '52.89.160.172:3128', '104.236.48.178:8080', '50.234.87.130:8080', '52.5.252.161:80', '199.227.40.28:80', '104.41.204.180:8888', '104.236.47.73:8080', '63.216.145.10:3128', '107.182.143.26:3128', '98.234.219.23:21320', '192.185.163.71:80', '50.87.151.198:8080', '168.63.24.174:8128', '107.170.88.22:3128', '104.131.80.169:3128', '104.131.240.143:3128', '50.240.46.244:7004', '162.243.9.201:3128']
proxz = list(reversed(proxz))

me.proxies = proxz

print(me.proxies)

print("start here")


def t1():
    for i in reversed(range(1,50)):
        n = int(random.random()*100)+1+50
        me.set(i,'lingerie+plus')
        time.sleep(3)
        me.get(i,'lingerieplus')
        time.sleep(n)

def t2():
    for i in reversed(range(1,50)):
        n = int(random.random()*100)+1+50
        me2.set(i,'panties')
        time.sleep(3)
        me2.get(i,'panties')
        time.sleep(n)

#print(me.gethtml("data.ht"))

def start():
    trd1 = Thread(target=t1)
    trd2 = Thread(target=t2)
    trd1.start()
    trd2.start()

start()
