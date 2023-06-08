'''As classes em Python são elementos que não são obrigatórios, mas ajudam a otimizar trechos dos códigos e também ajudam
no entendimento dos códigos.'''

# Vamos criar uma classe: Cachorro, definir alguns atributos dessa classe e também suas ações.

class Cachorro:
    def __init__(self, nome: str, raca: str, comprimento: float, peso: float):
        self.nome = nome
        self.raca = raca
        self.comprimento = comprimento
        self.peso = peso
    def latir(self):
        
        print(f'Au au! Eu sou o(a) {self.nome}')
    
    def moder(self):
        
        print(f'O(a) cachorro(a) {self.nome} te mordeu!')
   
    def dormir(self):
        
        print('ZzZzZz...')
    
    def brincar(self):
        
        print('Eu gosto de brincar de bolinha!')

    def comer(self):
        
        print(f'Eu peso {self.peso}kg e preciso comer {self.peso * 1000 * 0.01}g de comida para ficar satisfeito(a)')

'''Com esse código, definimos apenas a nossa classe, que equivale à nossa representação 
de um cachorro. Agora precisamos criar os nossos objetos. Para isso, 
usamos a seguinte sintaxe:'''

becca = Cachorro('Becca', 'West', 65, 7)

print(becca)

# <__main__.Cachorro object at 0x000001D2C336BD90>

becca.nome

# 'Becca'

becca.raca

# 'West'

type(becca)

# __main__.Cachorro

'''Agora, se quisermos criar uma nova instância de uma classe Cachorro, 
basta seguir o mesmo padrão:'''

milka = Cachorro('Milka', 'Biewer', 40, 2)

print(milka)

# <__main__.Cachorro object at 0x000001C12516BD30>

milka.latir()

# Au au! Eu sou o(a) Milka

becca.latir

# Au au! Eu sou o(a) Becca
