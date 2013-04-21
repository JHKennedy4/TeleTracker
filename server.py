import sys
from flask import Flask, request
import MySQLdb as mdb
import _mysql as mysql
import simplejson as json
import time
import datetime


class dbhelper:

	__dbhost = ""
	__dbname = ""
	__dbuser = ""
	__dbpass = ""

	__con = False

	def __init__(self):
		self.__load_credentials__()

	def __load_credentials__(self):

        	# read in credentials file
		lines = tuple(open('mysqlcreds.txt', 'r'))

		# set our local values
		self.__dbhost = lines[0].strip()
		self.__dbname = lines[1].strip()
		self.__dbuser = lines[2].strip()
		self.__dbpass = lines[3].strip()

		self.__con = mdb.connect(host=self.__dbhost, user=self.__dbuser, passwd=self.__dbpass, db=self.__dbname)

	def query_events(self, start, end):

		with self.__con:
			cur = self.__con.cursor()
			start = time.strptime(start, "%Y-%m-%d")
			start = datetime.datetime (start[0], start[1], start[2], start[3], start[4], start[5])
			end = time.strptime(end, "%Y-%m-%d")
			end = datetime.datetime (end[0], end[1], end[2], end[3], end[4], end[5])
			print start
			print end
			cur.execute("SELECT start_time, end_time, target FROM events WHERE start_time BETWEEN %s AND %s OR end_time BETWEEN %s AND %s", (start, end, start, end))
			rows = cur.fetchall()
			events = []
			for event in rows:
				mydata = (event[0].isoformat(),event[1].isoformat(),event[2])
				events.append(mydata)
			return events
	

app = Flask(__name__)
db = dbhelper();

@app.route("/satdata")
def satdata():
	start_date = request.args.get('start')
	end_date = request.args.get('end')
	
	if start_date != None and end_date != None:
		events = db.query_events(start_date, end_date)
		print events
		#return "hello"
		return json.dumps(events, indent = 2)

	else:
		return "You're missing some arguments there."

if __name__ == "__main__":
	app.run(debug=True)