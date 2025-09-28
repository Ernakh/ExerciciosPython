
from pathlib import Path

#Exercício 1
#Crie uma função em Python chamada par_ou_impar_arquivo que receba um número inteiro como entrada. 
#Esta função deve iterar de 1 até o número fornecido. Para cada número no intervalo, verifique se ele é par ou ímpar usando uma condicional. 
#Em seguida, escreva em um arquivo de texto chamado resultado_exercicio1.txt cada número e sua classificação ("é par" ou "é ímpar") em linhas separadas.

ARQ = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\resultado_exercicio1.txt")


def par_ou_impar_arquivo(numero: int):
    with open("resultado_exercicio1.txt", "w", encoding="utf-8") as arquivo:
        for i in range(1, numero + 1):
            if i % 2 == 0:
                arquivo.write(f"{i} é par\n")
            else:
                arquivo.write(f"{i} é ímpar\n")

par_ou_impar_arquivo(10)

print("--------------------------------------------------")

#Exercício 2
#Crie uma função Python chamada somar_numeros_arquivo que receba dois argumentos: o nome de um arquivo de texto de entrada e o nome de um arquivo de texto de saída. 
#O arquivo de entrada conterá números, um por linha. A função deve ler esses números, calcular a soma deles e escrever o resultado da soma em uma nova linha no arquivo de saída. 
#A função deve tratar possíveis erros, como o arquivo de entrada não ser encontrado ou linhas que não contenham números válidos.

ARQEntrada = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\")

def somar_numeros_arquivo(arquivo_entrada: str, arquivo_saida: str):
    soma = 0
    try:
        #print(str(ARQEntrada) + "\\" + arquivo_entrada)
        with open(str(ARQEntrada) + "\\" + arquivo_entrada, "r", encoding="utf-8") as entrada:
            for linha in entrada:
                try:
                    numero = float(linha.strip())
                    soma += numero
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")
        return

    with open(str(ARQEntrada) + "\\" + arquivo_saida, "a", encoding="utf-8") as saida:
        saida.write(f"Soma: {soma}\n")

somar_numeros_arquivo("entrada.txt", "saida.txt")

#Exercício 3
#Crie uma função Python chamada classificar_numeros_em_arquivo que receba como argumentos o nome 
# de um arquivo de texto de entrada e o nome de um arquivo de texto de saída. 
# O arquivo de entrada conterá números, um por linha. 
# A função deve ler esses números, classificar cada um como "Positivo", "Negativo" ou "Zero" e 
# escrever o número original e sua classificação em linhas separadas no arquivo de saída 
# exemplo -10: Negativo. A função deve tratar possíveis erros, como o arquivo de entrada não ser 
# encontrado ou linhas que não contenham números válidos.

def classificar_numeros_em_arquivo(arquivo_entrada: str, arquivo_saida: str):
    try:
        with open(str(ARQEntrada) + "\\" + arquivo_entrada, "r", encoding="utf-8") as entrada, \
             open(str(ARQEntrada) + "\\" + arquivo_saida, "w", encoding="utf-8") as saida:
            
            for linha in entrada:
                try:
                    numero = float(linha.strip())
                    
                    if numero > 0:
                        classificacao = "Positivo"
                    elif numero < 0:
                        classificacao = "Negativo"
                    else:
                        classificacao = "Zero"
                    
                    saida.write(f"{numero}:\n{classificacao}\n")
                
                except ValueError:
                    continue
    
    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")

classificar_numeros_em_arquivo("entrada.txt", "classificacao_saida.txt")


#Exercício 4
# Crie uma função Python chamada processar_dados_alunos que receba como argumento o nome de um arquivo de texto. 
# Este arquivo conterá dados de alunos no formato "Nome,Nota1,Nota2,Nota3", uma linha por aluno. 
# Dentro da função, abra o arquivo para leitura. Para cada linha do arquivo, leia o nome do aluno e suas três notas. 
# Calcule a média das três notas para cada aluno. Determine se o aluno foi aprovado (média >= 7.0) ou reprovado. 
# Crie um novo arquivo de texto chamado "resultados_alunos.txt". 
# Escreva no novo arquivo, para cada aluno, o nome e sua situação (Aprovado ou Reprovado) no formato "Nome: Situação". 
# A função deve tratar possíveis erros de arquivo não encontrado e linhas com formato inválido ou notas não numéricas.

def processar_dados_alunos(arquivo_entrada: str):
    try:
        with open(str(ARQEntrada) + "\\" + arquivo_entrada, "r", encoding="utf-8") as entrada, \
             open(str(ARQEntrada) + "\\" + "resultados_alunos.txt", "w", encoding="utf-8") as saida:

            for linha in entrada:
                try:
                    partes = linha.strip().split(",")
                    if len(partes) != 4:
                        continue
                    
                    nome = partes[0].strip()
                    notas = [float(nota.strip()) for nota in partes[1:]]
                    
                    media = sum(notas) / 3
                    
                    if media >= 7.0:
                        situacao = "Aprovado"
                    else:
                        situacao = "Reprovado"
                    
                    saida.write(f"{nome}: {situacao}\n")
                
                except Exception:
                    continue

    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")

processar_dados_alunos("dados_alunos.txt")

#Exercício 5
#Crie uma função Python chamada processar_vendas_manual que receba como argumentos o nome de um 
# arquivo CSV de entrada e o nome de um arquivo CSV de saída. 
# O arquivo de entrada conterá dados de vendas com as colunas "Produto", "Quantidade" e "Preco_Unitario".
#Dentro da função, abra o arquivo CSV de entrada para leitura. Leia cada linha do arquivo, 
# manualmente (sem usar bibliotecas como csv) dividindo a linha pelas vírgulas. 
# Para cada item de venda, calcule o "Valor_Total" multiplicando a "Quantidade" pelo "Preco_Unitario". 
# Certifique-se de converter "Quantidade" para inteiro e "Preco_Unitario" para float.
#Crie um novo arquivo CSV de saída. Para cada linha do arquivo de entrada , 
# escreva no arquivo de saída as informações originais ("Produto", "Quantidade", "Preco_unitario") 
# e o "Valor_Total" calculado, separando os valores por vírgulas.
#A função deve tratar possíveis erros, como arquivo de entrada não encontrado, 
# linhas com formato inválido ou valores não numéricos para Quantidade e Preco_Unitario.

def processar_vendas_manual(arquivo_entrada: str, arquivo_saida: str):
    try:
        with open(str(ARQEntrada) + "\\" + arquivo_entrada, "r", encoding="utf-8") as entrada, \
             open(str(ARQEntrada) + "\\" + arquivo_saida, "w", encoding="utf-8") as saida:

            cabecalho = entrada.readline().strip().split(",")
            if len(cabecalho) < 3:
                print("Cabeçalho inválido")
                return
            
            saida.write("Produto,Quantidade,Preco_Unitario,Valor_Total\n")

            for linha in entrada:
                try:
                    partes = linha.strip().split(",")
                    if len(partes) != 3:
                        continue
                    
                    produto = partes[0].strip()
                    quantidade = int(partes[1].strip())
                    preco_unitario = float(partes[2].strip())
                    
                    valor_total = quantidade * preco_unitario
                    
                    saida.write(f"{produto},{quantidade},{preco_unitario},{valor_total}\n")
                
                except Exception:
                    continue

    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")

processar_vendas_manual("vendas_entrada.csv", "vendas_saida.csv")
