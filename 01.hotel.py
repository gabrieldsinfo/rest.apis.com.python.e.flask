#1.1.HOTEL
#CLASSE CRUD C/ ATRIBUTOS E INSERT DE DADOS VIA JSON.
#from resources.hotel = CHAMANDO O ARQUIVO HOTEL
#import hoteis = IMPORTANDO A CLASSE HOTEIS/RECURSO
#reqparse = RECEBE OS ELEMENTOS JSON DA REQUISICAO
#pass = NAO PRECISA IMPLEMENTAR O CODIGO DE MOMENTO.
#get = BUSCAR
#post = CRIAR
#put = EDITAR / CRIAR
#del = APAGAR

from turtle import home
from flask_restful import Resource, reqparse
from models.hotelmodel import HotelModel


hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        },
        {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
        },
        {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Santa Catarina'
        }
]



class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}



class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')


    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None


    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404 #not found


    def post(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created / criado


    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 # OK
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created / criado


    def delete(self, hotel_id):
        global hoteis # referenciar a variavel já existente
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}


