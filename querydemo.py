from cartodb import CartoDBAPIKey, CartoDBException
import httplib2
httplib2.Http(disable_ssl_certificate_validation=True)
user =  'jhkennedy4@gmail.com'
API_KEY ='c3c310cb4bf016cd634e4df3d0a88b82826a4fbb'
cartodb_domain = 'jhk'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
        print cl.sql('select * from teletracker')
except CartoDBException as e:
        print ("some error ocurred", e)
