from flask import Flask
from cartodb import CartoDBAPIKey, CartoDBException
import json
app = Flask(__name__)
user =  'jhkennedy4@gmail.com'
API_KEY ='c3c310cb4bf016cd634e4df3d0a88b82826a4fbb'
cartodb_domain = 'jhk'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)


@app.route("/")
def hello():
    return cl.sql('select * from teletracker where cartodb_id = 2')


if __name__ == "__main__":
    app.run()

