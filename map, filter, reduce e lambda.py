# Exercício 1: Use map() e uma função definida para converter uma lista de strings em números inteiros.
def para_inteiro(s):
    return int(s)

strings = ["1", "2", "3", "4", "5"]
integers = list(map(int, strings))

numeros = list(map(para_inteiro, strings))

print(numeros)

# Exercício 2: Use map() e uma função definida para calcular o quadrado de cada número em uma lista.
numeros = [1, 2, 3, 4, 5]
def quadrado(n):
    return n ** 2

# Usando map() para aplicar a função em cada elemento da lista
quadrados = list(map(quadrado, numeros))

print(quadrados)

# Exercício 3: Use map() e uma função definida para adicionar o sufixo "_modificado" a cada string em uma lista.
palavras = ["casa", "carro", "cachorro"]

def adicionar_sufixo(palavra):
    return palavra + "_modificado"

palavras_modificadas = list(map(adicionar_sufixo, palavras))

print(palavras_modificadas)

# Exercício 4: Use map() e uma função definida para verificar se cada número em uma lista é positivo (retornar True ou False).
valores = [-1, 0, 5, -10, 100]

def eh_positivo(n):
    return n > 0

resultado = list(map(eh_positivo, valores))

print(resultado)


# Exercício 1: Use filter() e uma função definida para obter apenas as strings que começam com a letra 'c' de uma lista.
palavras = ["casa", "carro", "abacaxi", "cachorro", "elefante"]
def comeca_com_c(palavra):
    return palavra.startswith("c")

palavras_com_c = list(filter(comeca_com_c, palavras))

print(palavras_com_c)


# Exercício 2: Use filter() e uma função definida para obter apenas os números maiores que 10 de uma lista.
numeros = [5, 12, 8, 25, 3, 15]
def maior_que_dez(n):
    return n > 10

numeros_filtrados = list(filter(maior_que_dez, numeros))

print(numeros_filtrados)

# Exercício 3: Use filter() e uma função definida para obter apenas os elementos de uma lista que são do tipo string.
elementos = [1, "hello", True, 3.14, "world", False]
def eh_string(e):
    return isinstance(e, str)

strings = list(filter(eh_string, elementos))

print(strings)

# Exercício 4: Use filter() e uma função definida para obter apenas as palavras de uma lista que têm mais de 5 caracteres.
lista_palavras = ["python", "java", "c++", "javascript", "ruby"]
def mais_de_cinco_caracteres(palavra):
    return len(palavra) > 5

palavras_filtradas = list(filter(mais_de_cinco_caracteres, lista_palavras))

print(palavras_filtradas)

from functools import reduce
# Exercício 1: Use reduce() e uma função definida para encontrar o maior número em uma lista.
numeros = [10, 5, 20, 8, 15]
def maior(a, b):
    return a if a > b else b

maior_numero = reduce(maior, numeros)

print(maior_numero)

# Exercício 2: Use reduce() e uma função definida para concatenar todas as strings em uma lista.
palavras = ["programação", " ", "funcional", " ", "em", " ", "python"]
def concatenar(a, b):
    return a + b

frase = reduce(concatenar, palavras)

print(frase)

# Exercício 3: Use reduce() e uma função definida para calcular o fatorial de um número.
# Dica: Comece com um inicializador de 1.
numero_fatorial = 5

def multiplicar(a, b):
    return a * b

numeros = list(range(1, numero_fatorial + 1))

fatorial = reduce(multiplicar, numeros, 1)

print(f"O fatorial de {numero_fatorial} é {fatorial}")


# Exercício 4: Use reduce() e uma função definida para contar a ocorrência de um caractere específico em uma string.
string_para_contar = "programacao funcional"
caractere_alvo = "a"

def contar_caractere(acumulador, caractere):
    if caractere == caractere_alvo:
        return acumulador + 1
    else:
        return acumulador

quantidade = reduce(contar_caractere, string_para_contar, 0)

print(f"O caractere '{caractere_alvo}' aparece {quantidade} vezes.")


# Exercício 1: Use lambda para criar uma função que eleva um número ao quadrado.
quadrado = lambda x: x ** 2
print(quadrado(5))

# Exercício 2: Use lambda para criar uma função que verifica se uma string contém a letra 'e'.
contem_e = lambda s: 'e' in s

print(contem_e("python")) 
print(contem_e("Gremio")) 

# Exercício 3: Use lambda para criar uma função que concatena duas strings com um espaço no meio.
concatenar = lambda a, b: a + " " + b
print(concatenar("Grêmio", "Mundial de 1983"))

# Exercício 4: Use lambda para criar uma função que retorna o último elemento de uma lista.
ultimo_elemento = lambda lista: lista[-1]
print(ultimo_elemento([10, 20, 30, 40, 50]))

# Exercício 5: Use lambda com map() para converter uma lista de números em seus valores absolutos.
numeros = [-1, -2, 3, -4, 5]
valores_absolutos = list(map(lambda n: abs(n), numeros))
print(valores_absolutos)

# Exercício 6: Use lambda com filter() para obter apenas as palavras de uma lista que começam com vogal.
palavras = ["apple", "banana", "orange", "grape", "kiwi"]
palavras_com_vogal = list(filter(lambda p: p[0] in "aeiou", palavras))
print(palavras_com_vogal)

# Exercício 7: Use lambda com reduce() para encontrar o produto de todos os números em uma lista.
numeros = [1, 2, 3, 4, 5]
produto = reduce(lambda a, b: a * b, numeros)
print(produto)

# Exercício 8: Use lambda com sorted() para ordenar uma lista de dicionários pelo valor da chave 'idade'.
pessoas = [{"nome": "João", "idade": 30}, {"nome": "Maria", "idade": 25}, {"nome": "Pedro", "idade": 35}]
pessoas_ordenadas = sorted(pessoas, key=lambda p: p["idade"])
print(pessoas_ordenadas)

# Exercício 9: Use lambda para criar uma função que retorna True se um número for divisível por 3 e 5, e False caso contrário.
divisivel_por_3_e_5 = lambda n: n % 3 == 0 and n % 5 == 0
print(divisivel_por_3_e_5(15))
print(divisivel_por_3_e_5(9))
print(divisivel_por_3_e_5(10))

# Exercício 10: Use lambda para criar uma função que extrai o nome de usuário de um email (tudo antes do '@').
extrair_usuario = lambda email: email.split('@')[0]
print(extrair_usuario("fabricio.londero@facens.br"))
