import time
import random

def job():
    print("I'm working...")

for s in range(1,20):
    n = int(random.random()*100*60)+1+50
    print(n)
    job()
    time.sleep(2)
