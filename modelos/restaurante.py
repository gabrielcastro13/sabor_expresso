from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = [] 

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper() #upper, as palavras ficam maiusculas
        self._ativo = False #O underline '_' nao permite que os dados desse atributo sejam alterados, ele se torna privado 
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliacao' 
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self,item): #adicionar item no cardapio
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property #valor que queremos ler
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}\n')
        for i,item in enumerate(self._cardapio,start=1): #i=indice
            if hasattr(item,'descricao'): 
                mensagem_prato = f'{i}. Nome:{item._nome} | Preco: R${item._preco} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preco: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
