#1.0.APP
#CLASSE PRINCIPAL C/ IMPORT DE LIBS FLASK, REFATORACAO E RECURSOS.
#from resources.hotel = CHAMANDO O ARQUIVO HOTEL
#import hoteis = IMPORTANDO A CLASSE HOTEIS/RECURSO

from flask import Flask 
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__== '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000   
