import bayclass as e
import time
import random

# Set Initial Proxy to Get New Proxies
me = e.Bay("111.14.40.155:8081")

# Get New Proxies
me.getips()
print(me.proxies)

# Or Use Your Own Proxies
# me.proxies = ['52.27.149.22:80','161.68.250.139:80','161.68.250.181:8080']

for i in reversed(range(1,47)):
    n = int(random.random()*100)+1+50
    me.set(i,'sexy+one+size')
    time.sleep(3)
    me.get(i,'sexyonesize')
    time.sleep(n)
