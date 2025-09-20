from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []  # lista para armazenar objetos Avaliacao
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} / {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} / {'Categoria'.ljust(25)} / {'Avaliação'.ljust(25)} / {'Status'}")
        for restaurante in cls.restaurantes:
            media_str = f"{restaurante.media_avaliacoes:.1f}".ljust(25)  # converte float para string formatada
            print(f"{restaurante._nome.ljust(25)} / {restaurante._categoria.ljust(25)} / {media_str} / {restaurante.ativo}")
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property  
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes )
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media

    
# print(restaurante_praca.ativo)
# f restaurante_pizza.ativo == False:
#    print('O restaurante está ativo')
# else:
 #   print('O restaurante está inativo')

# print(dir(restaurante_praca)) - mostra tudo do objeto
# print(vars(restaurante_praca)) # atributos do objeto
# print(restaurante_praca.nome)