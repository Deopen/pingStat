#! /usr/bin/env python3.8
#showing ping delay in Mac menu bar

#for installing requirements: rumps , pebble and ping3
#pip3.8 install -r pingStatRequirements.txt

#don't forget chmod 755
#sudo python3.8 pingStat.py or
#sudo ./pingStat.py
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
    mem=[]
    prc=""
    while 1==1:
        time.sleep(1)
        try:
            l=ping('8.8.8.8',ttl=109,size=64,unit='ms')
            if type(l)==float:
                l=int(l*100)
                l=l/100.0

            if l==None:
                l="Lost"
                mem.append(0)
            else:
                mem.append(1)
            if len(mem)>100:
                mem=mem[1:]
                prc="%"

        except:
            l="!"
        #PLR = Packet Loss Ratio
        x.title=str(l)+" PLR: "+str(mem.count(0))+prc



updateTitle()
x.run()
