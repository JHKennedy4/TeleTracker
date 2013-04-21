from flask import Flask
from flask import render_template
from cartodb import CartoDBAPIKey, CartoDBException
import simplejson as json
app = Flask(__name__)
user =  'jhkennedy4@gmail.com'
API_KEY ='c3c310cb4bf016cd634e4df3d0a88b82826a4fbb'
cartodb_domain = 'jhk'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)


@app.route("/")
def index():
	#data = cl.sql('select * from teletracker where cartodb_id = 2')
	return render_template('app/index.html') #json.dumps(data, indent = 2)

if __name__ == "__main__":
    app.run(debug=True)

