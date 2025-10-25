#Exercício: Análise Manual do Dataset Disney+
#Objetivo:
#Este exercício tem como objetivo desenvolver suas habilidades em manipulação manual de dados em Python, 
# processando um dataset de shows da Disney+ sem o auxílio de bibliotecas de parsing como csv ou pandas. 
# Você deverá extrair informações relevantes e gerar um relatório detalhado.

#Dataset:
#O dataset a ser utilizado está disponível no seguinte link: https://www.kaggle.com/datasets/eshummalik/disney

#Instruções:
#Download do Dataset: Baixe o arquivo do dataset manualmente a partir do link fornecido. - ok
#Carregamento Manual dos Dados:
#Implemente uma função chamada abrir_filmes_disney() que será responsável por abrir o arquivo do dataset.  - ok

#Você não deve utilizar bibliotecas como csv ou pandas para ler o arquivo.   - ok
# A leitura deve ser feita linha por linha, utilizando as funcionalidades básicas de manipulação de arquivos em Python. - ok
#Ignore linhas vazias encontradas no arquivo. - ok

#Para cada linha do dataset, identifique se ela representa um filme (type coluna) ou uma série. - ok
#Crie duas classes em Python: Filme e Serie. - ok
# Cada linha do dataset deve ser mapeada para uma instância da classe Filme ou Serie correspondente, -ok
# contendo seus respectivos atributos (baseados nas colunas do dataset). - ok
# Implemente getters e setters para os atributos conforme necessário. - ok
#Os campos que contêm o valor "N/A" no dataset devem ser tratados e armazenados como None nos objetos Filme ou Serie. - ok

#A função abrir_filmes_disney() deve retornar uma lista contendo todos os objetos Filme e Serie criados a partir do dataset. - ok
#Certifique-se de que o arquivo do dataset seja devidamente fechado ao final da execução da função abrir_filmes_disney(). - ok

#Geração do Relatório:
#Implemente uma função chamada gerar_relatorio() - ok
# que receberá como entrada a lista de objetos Filme e Serie retornada pela função abrir_filmes_disney(). - ok
#Com base nos dados contidos nos objetos, calcule e inclua no relatório as seguintes informações:

#A média da nota de todos os filmes no IMDB. - ok
#A média da nota de todos os filmes no Metascore. - ok
#A média do número de votos de todos os filmes no IMDB. - ok
#As 3 línguas mais usadas e as 3 línguas menos usadas no dataset. - ok
#Os 3 atores que mais aparecem e os 3 atores que menos aparecem no dataset. - ok
#O diretor com mais filmes no dataset. - ok
#O diretor com o filme mais popular no IMDB (considerando a maior nota IMDB). -  ok
#O diretor com o filme mais popular no Metascore (considerando a maior nota Metascore). - ok
#O ano em que mais filmes foram lançados. - ok
#A pior série segundo a nota IMDB e a pior série segundo a nota Metascore.  -  ok
#Uma lista de filmes que possuem mais de um lançamento (considerados "remakes" 
# ou diferentes versões no dataset, identificados por títulos iguais mas anos de lançamento diferentes). - ok?
#O relatório de saída deve ser salvo em um arquivo texto chamado relatorio-disney.txt no mesmo diretório do script.
#Estrutura do Código: Organize seu código de forma modular, utilizando as funções abrir_filmes_disney() e gerar_relatorio() - ok
#conforme especificado. Você não é obrigado a passar parâmetros para essas funções, mas pode fazê-lo se julgar necessário para uma melhor organização do código. - ok

from pathlib import Path
from typing import List
import pandas as pd
import numpy as np
from IPython.display import display

ARQ = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\Trabalho\\disney_plus_shows.csv")
ARQSaida = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\Trabalho\\relatorio-disney-pandas.txt")

class Obra:
    def __init__(self, imdb_id, titulo, plot, rated, ano, lancamento, adicionado, duracao, genero, diretor, escritor, atores, idioma, pais, premios, metascore, imdb_rating, imdb_votes):
        self.set_imdb_id(imdb_id)
        self.set_titulo(titulo)
        self.set_plot(plot)
        self.set_rated(rated)
        self.set_ano(ano)
        self.set_lancamento(lancamento)
        self.set_adicionado(adicionado)
        self.set_duracao(duracao)
        self.set_genero(genero)
        self.set_diretor(diretor)
        self.set_escritor(escritor)
        self.set_atores(atores)
        self.set_idioma(idioma)
        self.set_pais(pais)
        self.set_premios(premios)
        self.set_metascore(metascore)
        self.set_imdb_rating(imdb_rating)
        self.set_imdb_votes(imdb_votes)

    def get_imdb_id(self):
        return self.imdb_id
    def set_imdb_id(self, imdb_id):
        self.imdb_id = imdb_id != "N/A" and imdb_id or None
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):   
        self.titulo = titulo != "N/A" and titulo or None
    def get_plot(self):
        return self.plot
    def set_plot(self, plot):
        self.plot = plot != "N/A" and plot or None
    def get_rated(self):
        return self.rated
    def set_rated(self, rated):
        self.rated = rated != "N/A" and rated or None
    def get_ano(self):
        return self.ano
    def set_ano(self, ano):
        self.ano = ano != "N/A" and ano or None
    def get_lancamento(self):
        return self.lancamento
    def set_lancamento(self, lancamento):
        self.lancamento = lancamento != "N/A" and lancamento or None
    def get_adicionado(self):
        return self.adicionado
    def set_adicionado(self, adicionado):   
        self.adicionado = adicionado != "N/A" and adicionado or None
    def get_duracao(self):
        return self.duracao
    def set_duracao(self, duracao):
        self.duracao = duracao != "N/A" and duracao or None
    def get_genero(self):
        return self.genero
    def set_genero(self, genero):
        self.genero = genero != "N/A" and genero or None
    def get_diretor(self):
        return self.diretor
    def set_diretor(self, diretor):
        self.diretor = diretor  != "N/A" and diretor or None
    def get_escritor(self):
        return self.escritor
    def set_escritor(self, escritor):
        self.escritor = escritor != "N/A" and escritor or None
    def get_atores(self):
        return self.atores
    def set_atores(self, atores):
        self.atores = atores != "N/A" and atores or None
    def get_idioma(self):
        return self.idioma  
    def set_idioma(self, idioma):
        self.idioma = idioma != "N/A" and idioma or None
    def get_pais(self):
        return self.pais
    def set_pais(self, pais):
        self.pais = pais != "N/A" and pais or None
    def get_premios(self):
        return self.premios
    def set_premios(self, premios):
        self.premios = premios != "N/A" and premios or None
    def get_metascore(self):
        return self.metascore   
    def set_metascore(self, metascore):
        self.metascore = metascore != "N/A" and metascore or None
    def get_imdb_rating(self):  
        return self.imdb_rating
    def set_imdb_rating(self, imdb_rating):
        self.imdb_rating = imdb_rating != "N/A" and imdb_rating or None
    def get_imdb_votes(self):
        return self.imdb_votes
    def set_imdb_votes(self, imdb_votes):
        self.imdb_votes = imdb_votes != "N/A" and imdb_votes or None

class Serie (Obra):
    pass
class Filme (Obra):
    pass

# df_filmes = None
# df_series = None

def abrir_filmes_disney():
    
    global df, df_filmes, df_series
    
    df = pd.read_csv(ARQ)
    #display(df)
    
    
    df_filmes = df[df.iloc[:, 3] == "movie"].copy()
    df_series = df[df.iloc[:, 3] == "series"].copy()
    
    display(df_filmes)
    #display(df_series)
    
def gerar_relatorio():
    
    file = open(ARQSaida, "w", encoding="utf-8")
    
    file.write("Relatórios Disney\n")
    file.write("=================\n\n")
    file.write(f"Total de obras: {len(df)}\n")  
    file.write(f"Total de filmes: {len(df_filmes)}\n")
    file.write(f"Total de séries: {len(df_series)}\n\n")

    print("Relatórios Disney\n")
    print("=================\n\n")
    print(f"Total de obras: {len(df)}\n")
    print(f"Total de filmes: {len(df_filmes)}\n")
    print(f"Total de séries: {len(df_series)}\n")
    
    #A média da nota de todos os filmes no IMDB.
    media_imdb = df_filmes['imdb_rating'].replace("N/A", np.nan).astype(float).mean()
    print(f"Média da nota de todos os filmes no IMDB: {media_imdb:.2f}")
    file.write(f"Média da nota de todos os filmes no IMDB: {media_imdb:.2f}\n")
    
    #A média da nota de todos os filmes no Metascore.
    media_metascore = df_filmes['metascore'].replace("N/A", np.nan).astype(float).mean()
    print(f"Média da nota de todos os filmes no Metascore: {media_metascore:.2f}")
    file.write(f"Média da nota de todos os filmes no Metascore: {media_metascore:.2f}\n")
    
    #A média do número de votos de todos os filmes no IMDB.
    media_votes = df_filmes['imdb_votes'].replace("N/A", np.nan).str.replace(',', '').astype(float).mean()
    print(f"Média do número de votos de todos os filmes no IMDB: {media_votes:.2f}")
    file.write(f"Média do número de votos de todos os filmes no IMDB: {media_votes:.2f}\n")
    
    #As 3 línguas mais usadas e as 3 línguas menos usadas no dataset.
    idiomas = df['language'].dropna().str.split(', ').explode()
    mais_usadas = idiomas.value_counts().head(3)
    menos_usadas = idiomas.value_counts().tail(3)
    file.write(f"3 línguas mais usadas:\n{mais_usadas}\n")
    file.write(f"3 línguas menos usadas:\n{menos_usadas}\n")
    print(f"3 línguas mais usadas:\n{mais_usadas}\n")
    print(f"3 línguas menos usadas:\n{menos_usadas}\n")
    
    #Os 3 atores que mais aparecem e os 3 atores que menos aparecem no dataset.
    atores = df['actors'].dropna().str.split(', ').explode()
    mais_atores = atores.value_counts().head(3)
    menos_atores = atores.value_counts().tail(3)
    file.write(f"3 atores que mais aparecem:\n{mais_atores}\n")
    file.write(f"3 atores que menos aparecem:\n{menos_atores}\n")
    print(f"3 atores que mais aparecem:\n{mais_atores}\n")
    print(f"3 atores que menos aparecem:\n{menos_atores}\n")
    
    #O diretor com mais filmes no dataset.
    diretores = df_filmes['director'].dropna()
    diretor_mais_filmes = diretores.value_counts().idxmax()
    file.write(f"Diretor com mais filmes no dataset: {diretor_mais_filmes}\n")
    print(f"Diretor com mais filmes no dataset: {diretor_mais_filmes}\n")
    
    #O diretor com o filme mais popular no IMDB (considerando a maior nota IMDB).
    df_filmes['imdb_rating'] = pd.to_numeric(df_filmes['imdb_rating'], errors='coerce')
    diretor_melhor_imdb = df_filmes.loc[df_filmes['imdb_rating'].idxmax()]['director']
    file.write(f"Diretor com o filme mais popular no IMDB: {diretor_melhor_imdb}\n") 
    print(f"Diretor com o filme mais popular no IMDB: {diretor_melhor_imdb}\n")
    
    #O diretor com o filme mais popular no Metascore (considerando a maior nota Metascore).
    df_filmes['metascore'] = pd.to_numeric(df_filmes['metascore'], errors='coerce')
    diretor_melhor_metascore = df_filmes.loc[df_filmes['metascore'].idxmax()]['director']
    file.write(f"Diretor com o filme mais popular no Metascore: {diretor_melhor_metascore}\n")  
    print(f"Diretor com o filme mais popular no Metascore: {diretor_melhor_metascore}\n")
    
    #O ano em que mais filmes foram lançados.
    anos_lancamento = df_filmes['year'].dropna().astype(int)    
    ano_mais_filmes = anos_lancamento.value_counts().idxmax()
    file.write(f"Ano em que mais filmes foram lançados: {ano_mais_filmes}\n")
    print(f"Ano em que mais filmes foram lançados: {ano_mais_filmes}\n")
    
    #A pior série segundo a nota IMDB e a pior série segundo a nota Metascore.    
    #df_series['imdb_rating'] = pd.to_numeric(df_series['imdb_rating'], errors='coerce')
    #pior_serie_imdb = df_series.loc[df_series['imdb_rating'].idxmin()]['title']
    df_series_imdb_validas = df_series.dropna(subset=['imdb_rating'])

    pior_serie_imdb_titulo = None
    pior_serie_imdb_nota = None
    
    if not df_series_imdb_validas.empty:
        pior_serie_imdb_row = df_series_imdb_validas.sort_values(by='imdb_rating', ascending=True).iloc[0]
        
        pior_serie_imdb_titulo = pior_serie_imdb_row['title']
        pior_serie_imdb_nota = pior_serie_imdb_row['imdb_rating']
    file.write(f"Pior série segundo a nota IMDB: {pior_serie_imdb_titulo} - {pior_serie_imdb_nota}\n")
    print(f"Pior série segundo a nota IMDB: {pior_serie_imdb_titulo} - {pior_serie_imdb_nota}\n")
    
    #df_series['metascore'] = pd.to_numeric(df_series['metascore'], errors='coerce')
    #pior_serie_metascore = df_series.loc[df_series['metascore'].idxmin()]['title']
    df_series['metascore'] = pd.to_numeric(df_series['metascore'], errors='coerce')

    # 2. Filtra as séries que possuem um Metascore válido
    df_series_meta_validas = df_series.dropna(subset=['metascore'])

    pior_serie_metascore_titulo = None
    pior_serie_metascore_nota = None
    
    if not df_series_meta_validas.empty:
        pior_serie_metascore_row = df_series_meta_validas.sort_values(by='metascore', ascending=True).iloc[0]
        
        pior_serie_metascore_titulo = pior_serie_metascore_row['title']
        pior_serie_metascore_nota = pior_serie_metascore_row['metascore']
    file.write(f"Pior série segundo a nota Metascore: {pior_serie_metascore_titulo} - {pior_serie_metascore_nota}\n")   
    print(f"Pior série segundo a nota Metascore: {pior_serie_metascore_titulo} - {pior_serie_metascore_nota}\n")     
    
    #Uma lista de filmes que possuem mais de um lançamento (considerados "remakes"
    titulos_duplicados = df_filmes[df_filmes.duplicated(subset=['title'], keep=False)]
    if not titulos_duplicados.empty:        
        filmes_remakes = titulos_duplicados['title'].unique()
        file.write("Filmes com mais de um lançamento:\n")
        print("Filmes com mais de um lançamento:")
        for filme in filmes_remakes:
            file.write(f"- {filme}\n")   
            print(f"- {filme}")   
    else:
        file.write("Nenhum filme com múltiplos lançamentos encontrado.\n")  
        print("Nenhum filme com múltiplos lançamentos encontrado.")        
    
    file.close()        
    
abrir_filmes_disney()
gerar_relatorio()
