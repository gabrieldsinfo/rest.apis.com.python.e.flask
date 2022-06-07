#02.HOTEL
#CLASSE CRUD COM ATRIBUTOS.
#reqparse = RECEBE OS ELEMENTOS JSON DA REQUISICAO

#EXEMPLO DE ARQUIVO JSON UTILIZADO NO METODO POST PARA TESTES VIA API:
"""
            {
            "nome": "Bravo Hotel",
            "estrelas": 2.2,
            "diaria": 222.34,
            "cidade": "Sao Paulo"
            }
"""

from flask_restful import Resource, reqparse
from models.hotelmodels import HotelModel
from flask_jwt_extended import jwt_required

#EXEMPLO DE ARQUIVO JSON UTILIZADO NO METODO POST HOTEIS PARA TESTES VIA API:
"""
            {
            "nome": "Bravo Hotel",
            "estrelas": 2.2,
            "diaria": 222.34,
            "cidade": "Sao Paulo"
            }
"""

class Hoteis(Resource):
    def get(self):
        return{'hoteis':[hotel.json() for hotel in HotelModel.query.all()]} #SELECT * FROM Hoteis

class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="Esse campo 'NOME' não pode ser deixado em branco") #NAO PODERA ENVIAR JSON SEM O NOME
    atributos.add_argument('estrelas', type=float, required=True, help="Esse campo 'ESTRELAS' não pode ser deixado em branco")
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #not found


    @jwt_required() #Significa que o post será requirido ou seja, será necessário estar logado.
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400 #Badrequest

        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Houve um erro interno ao tentar salvar o HOTEL.'}, 500 #INTERNAL SERVER ERROR
        return hotel.json()


    @jwt_required()   
    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 # OK
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Houve um erro interno ao tentar salvar o HOTEL.'}, 500 #INTERNAL SERVER ERROR
        return hotel.json(), 201


    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Houve um erro interno ao deletar o HOTEL.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404