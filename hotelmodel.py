#CRIANDO O CONSTRUTOR E TEREMOS UM OBJETO QUANDO FOR ESTANCIAR A CLASSE HOTELMODEL
class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade


    # METODO QUE TRANSFORMA ESSE OBJETO EM DICIONARIO
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.estrelas,
            'cidade': self.cidade
        }