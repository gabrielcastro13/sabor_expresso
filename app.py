from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gabriel', 7)
restaurante_praca.receber_avaliacao('Alaor', 3)
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Flocos', 8.00, 'Sorvete', 'grande', 'o mais saboroso')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()