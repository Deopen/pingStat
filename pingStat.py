#! python3.8
#showing ping delay in Mac menu bar
#don't forget chmod 755
#sudo python3.8 pingStat.py
#written by omid yaghoubi
#deopenmail@gmail.com

import rumps
import time
from pebble import concurrent
from ping3 import ping

class pingStat(rumps.App):
    pass



x=pingStat("po")

@concurrent.thread
def updateTitle():
    for i in range(7000):
        time.sleep(1)
        try:
            l=ping('8.8.8.8',ttl=109,size=32,unit='ms')
        except:
            l="!"
        if type(l)==float:
            l=int(l*100)
            l=l/100.0

        x.title=str(l)



updateTitle()
x.run()
