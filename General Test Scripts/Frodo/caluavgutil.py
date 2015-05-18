import json
import urllib2
import socket
import time
import socket

def caluavgutil():
	
	jsondata=json.load(urllib2.urlopen('http://visualizee.die.upm.es:8000/render/?&target=keepLastValue(visualizee.greencpd.openstackTest.rack.r01.server.*.aggregation.cpu-average.cpu.user)&format=json&from=-1min'))

	avg=0
	for i in range(0,len(jsondata)):
		for j in range(0,len(jsondata[i]['datapoints'])):
			try:
				avg+=jsondata[i]['datapoints'][j][0]
			except:
				avg+=avg/(i*j)
	return avg/24

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('visualizee.die.upm.es', 3003))

while(1):
	s.sendall('visualizee.greencpd.openstackTest.rack.r01.server.cpu-util-avg ' + str(caluavgutil()) + ' ' + str(int(time.time())))
	time.sleep(5)

