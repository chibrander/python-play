import bayclass as e
import time
import random

for i in reversed(range(1,50)):
    n = int(random.random()*100)+1+50
    e.bay.make(i)
    time.sleep(3)
    e.bay.get(i,'file')
    time.sleep(n)
