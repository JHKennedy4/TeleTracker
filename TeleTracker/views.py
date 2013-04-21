from flask import Flask, render_template
from TeleTracker import TeleTracker
from cartodb import CartoDBAPIKey, CartoDBException
import simplejson as json
user =  'jhkennedy4@gmail.com'
API_KEY ='c3c310cb4bf016cd634e4df3d0a88b82826a4fbb'
cartodb_domain = 'jhk'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)

    #data = cl.sql('select * from teletracker where cartodb_id = 2')
#json.dumps(data, indent = 2)
@TeleTracker.route('/')
def index():
	return render_template('index.html')
