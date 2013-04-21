import re
import urllib
import urllib2
from xml import dom
from itertools import islice

class DataPoint:
	def __init__(self, sequenceNumber, obsID, constr, target, start, time, si, grat, ra, dec, roll, pitch, slew):
		self.sequenceNumber = sequenceNumber
		self.obsID = obsID
		self.constr = constr
		self.target = target
		self.start = start
		self.time = time
		self.si = si
		self.grat = grat
		self.ra = ra
		self.dec = dec
		self.roll = roll
		self.pitch = pitch
		self.slew = slew

#markers for the beginning and end of the schedule block
TRIGGER = "<pre id=\"schedule\">"
QUITTER = "</pre id=\"schedule\">"

#open the page
url = urllib2.urlopen("http://asc.harvard.edu/target_lists/stscheds/index.html")
start_seen = False
schedule = ""

for line in url:
	if line.strip() == QUITTER:
		break
	if line.strip() == TRIGGER:
		start_seen = True
		continue
	if start_seen == True:
		schedule = schedule + line

#print schedule
elements = list()
for line in schedule.splitlines():
	elements = line.split()
	print elements[3]
	'''
	if elements[0] == "<a":
		sequenceNumber = elements[1]
		sequenceNumber = sequenceNumber[:-4]
		print sequenceNumber
	'''