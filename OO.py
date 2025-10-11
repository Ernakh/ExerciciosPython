# Exercício 1: Crie uma classe base 'Veiculo' com atributos 'marca' e 'modelo' e um método 'acelerar'.
# Crie uma classe filha 'Carro' que herda de 'Veiculo' e adicione um método 'ligar_radio'.
# Crie uma instância de Carro e use métodos de ambas as classes.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O veículo {self.marca} {self.modelo} está acelerando")

class Carro(Veiculo):
    def ligar_radio(self):
        print(f"O rádio do {self.marca} {self.modelo} foi ligado")

meu_carro = Carro("Ford", "Ecosport")

meu_carro.acelerar()
meu_carro.ligar_radio()   

# Exercício 2: Crie uma classe base 'FormaGeometrica' com um método 'calcular_area'.
# Crie classes filhas 'Circulo' e 'Quadrado' que herdam de 'FormaGeometrica'.
# Sobrescreva o método 'calcular_area' em cada classe filha para calcular a área da forma correspondente.

import math

class FormaGeometrica:
    def calcular_area(self):
        return

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return area

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado ** 2
        return area

circulo = Circulo(5)
quadrado = Quadrado(4)

print(f"Área do círculo: {circulo.calcular_area():.2f}")
print(f"Área do quadrado: {quadrado.calcular_area():.2f}")

# Exercício 1: Crie uma classe base 'Forma' com um método 'desenhar'.
# Crie classes filhas 'Circulo' e 'Quadrado' que herdam de 'Forma'.
# Sobrescreva o método 'desenhar' em cada classe filha para imprimir uma mensagem indicando que está desenhando um círculo ou um quadrado.
# Crie uma lista com instâncias de Circulo e Quadrado e itere sobre ela chamando o método 'desenhar'.

class Forma:
    def desenhar(self):
        return

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo")

class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado")

formas = [Circulo(), Quadrado(), Circulo(), Quadrado()]

for forma in formas:
    forma.desenhar()


# Exercício 2: Crie uma classe base 'Pagamento' com um método 'processar_pagamento'.
# Crie classes filhas 'CartaoCredito', 'PayPal' e 'TransferenciaBancaria' que herdam de 'Pagamento'.
# Sobrescreva o método 'processar_pagamento' em cada classe filha para imprimir uma mensagem específica para cada método de pagamento.
# Crie uma lista de diferentes tipos de pagamento e processe cada um em um loop.

class Pagamento:
    def processar_pagamento(self, valor):
        return

class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via Cartão de Crédito")

class PayPal(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via PayPal")

class TransferenciaBancaria(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via Transferência Bancária")

pagamentos = [
    CartaoCredito(),
    PayPal(),
    TransferenciaBancaria()
]

for pagamento in pagamentos:
    pagamento.processar_pagamento(150.00)


# Exercício 1: Crie uma classe 'Produto' com atributos "privados" __nome e __preco.
# Implemente métodos públicos (getters) para acessar esses atributos e um método público (setter) para modificar o preço, garantindo que o novo preço seja positivo.
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome  
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print(f"Preço atualizado para R${novo_preco:.2f}")
        else:
            print("Erro: o preço deve ser positivo!")

produto = Produto("Notebook", 3500.00)
print(f"Produto: {produto.get_nome()} - Preço: R${produto.get_preco():.2f}")

produto.set_preco(4000.00)
print(f"Novo preço: R${produto.get_preco():.2f}")

# Exercício 2: Crie uma classe 'Funcionario' com atributo "privado" __salario.
# Implemente um método público 'aumentar_salario' que receba um percentual e aumente o salário, e um método público 'get_salario' para retornar o salário atual.
class Funcionario:
    def __init__(self, salario):
        self.__salario = salario

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.__salario * (percentual / 100)
            self.__salario += aumento
            print(f"Salário aumentado em {percentual}%! Novo salário: R${self.__salario:.2f}")
        else:
            print("Erro: o percentual de aumento deve ser positivo!")

    def get_salario(self):
        return self.__salario


func = Funcionario(3000.00)
print(f"Salário atual: R${func.get_salario():.2f}")

func.aumentar_salario(10)
print(f"Após aumento: R${func.get_salario():.2f}")

# Exercício 1: Use List Comprehension para criar uma nova lista contendo o quadrado de cada número na lista 'numeros'.
numeros = [1, 2, 3, 4, 5]
quadrados = [n**2 for n in numeros]
print(quadrados)

# Exercício 2: Use List Comprehension para criar uma nova lista contendo apenas as strings da lista 'elementos'.
elementos = [1, "hello", True, 3.14, "world", False]
strings = [e for e in elementos if isinstance(e, str)]
print(strings)

# Exercício 3: Use List Comprehension para criar uma nova lista contendo apenas os números pares da lista 'numeros'.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)

# Exercício 4: Use List Comprehension para criar uma nova lista contendo o comprimento de cada palavra na lista 'palavras'.
palavras = ["python", "java", "c++", "javascript", "ruby"]
comprimentos = [len(p) for p in palavras]
print(comprimentos)
