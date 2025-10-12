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

ARQ = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\Trabalho\\disney_plus_shows.csv")
ARQSaida = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\Trabalho\\relatorio-disney.txt")

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

Obras: List[Obra] = []  
Filmes: List[Filme] = []
Series: List[Serie]= []

def parse_csv_line(line: str, sep: str = ","):
    campos = []
    atual = []
    em_aspas = False
    i = 0
    while i < len(line):
        ch = line[i]
        if em_aspas:
            if ch == '"':
                if i + 1 < len(line) and line[i + 1] == '"':
                    atual.append('"')
                    i += 2
                else:
                    em_aspas = False
                    i += 1
            else:
                atual.append(ch)
                i += 1
        else:
            if ch == '"':
                em_aspas = True
                i += 1
            elif ch == sep:
                campos.append("".join(atual))
                atual = []
                i += 1
            else:
                if ch not in ("\r", "\n"):
                    atual.append(ch)
                i += 1
    campos.append("".join(atual))
    return campos

def abrir_filmes_disney():
    with open(ARQ, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                #colunas = linha.strip().split(",") #erro - exietem viruglas dentro de alguams colunas
                colunas = parse_csv_line(linha)
                #print(colunas)
                if colunas[3] == "movie":
                    filme = Filme(colunas[0], colunas[1], colunas[2], colunas[4], colunas[5], colunas[6], colunas[7], colunas[8], colunas[9], colunas[10], colunas[11], colunas[12], colunas[13], colunas[14], colunas[15], colunas[16], colunas[17], colunas[18])
                    Filmes.append(filme)
                    Obras.append(filme)
                elif colunas[3] == "series":
                    serie = Serie(colunas[0], colunas[1], colunas[2], colunas[4], colunas[5], colunas[6], colunas[7], colunas[8], colunas[9], colunas[10], colunas[11], colunas[12], colunas[13], colunas[14], colunas[15], colunas[16], colunas[17], colunas[18])
                    Series.append(serie)   
                    Obras.append(serie) 
    f.close()
    return Obras

def gerar_relatorio(Obras: List[Obra]):
    
    with open(ARQSaida, "w", encoding="utf-8") as file:
        file.write("Relatórios Disney\n")
        file.write("=================\n\n")
        file.write(f"Total de obras: {len(Obras)}\n")  
        file.write(f"Total de filmes: {len(Filmes)}\n")
        file.write(f"Total de séries: {len(Series)}\n\n")
    
        print("Relatórios Disney\n")
        print("=================\n\n")
        print(f"Total de obras: {len(Obras)}\n")
        print(f"Total de filmes: {len(Filmes)}\n")
        print(f"Total de séries: {len(Series)}\n")

        #A média da nota de todos os filmes no IMDB.
        aux = 0
        cont = 0
        for f in Filmes:
            if f.get_imdb_rating() != None:
                aux += float(f.get_imdb_rating())
                cont += 1
        imdb_media = aux / cont
        print(f"Média IMDB: {imdb_media}\n")
        file.write(f"Média IMDB: {imdb_media}\n\n")

        #A média da nota de todos os filmes no Metascore.
        aux = 0
        cont = 0
        for f in Filmes:
            if f.get_metascore() != None:
                aux += float(f.get_metascore())
                cont += 1
        metascore_media = aux / cont
        print(f"Média Metascore: {metascore_media}\n")
        file.write(f"Média Metascore: {metascore_media}\n\n")
        
        #A média do número de votos de todos os filmes no IMDB.
        aux = 0
        cont = 0
        for f in Filmes:
            #f: Filme
            if f.get_imdb_votes() != None:
                aux += float(f.get_imdb_votes().replace(',', '').replace('.', ''))
                cont += 1
        votos_media = aux / cont
        print(f"Média de votos Imdb: {votos_media}\n")
        file.write(f"Média de votos Imdb: {votos_media}\n\n")
        
        #As 3 línguas mais usadas e as 3 línguas menos usadas no dataset.
        idiomas_count = {}
        
        for o in Obras:
            if o.get_idioma() != None:
                idiomas = o.get_idioma().split(", ")
                for idioma in idiomas:
                    idioma = idioma.strip()
                    if idioma in idiomas_count:
                        idiomas_count[idioma] += 1
                    else:
                        idiomas_count[idioma] = 1
        
        if idiomas:
            ##mais_usadas = idiomas.most_common(3)
            #menos_usadas = idiomas.most_common()[:-4:-1]  # últimas 3
            idiomas_ordenados = sorted(idiomas_count.items(), key=lambda x: x[1], reverse=True)

            mais_usadas = idiomas_ordenados[:3]
            menos_usadas = idiomas_ordenados[-3:]
            
            print("3 idiomas que mais aaprecem:")
            file.write("3 idiomas que mais aparecem:\n")
            for idioma, qtd in mais_usadas:
                print(f" - {idioma}: {qtd}")
                file.write(f" - {idioma}: {qtd}\n")

            print("3 idiomas menos aparecem:")
            file.write("3 idiomas que menos aparecem:\n")
            for idioma, qtd in menos_usadas:
                print(f" - {idioma}: {qtd}")
                file.write(f" - {idioma}: {qtd}\n")
        
        #Os 3 atores que mais aparecem e os 3 atores que menos aparecem no dataset.
        atores_count = {}
        
        for o in Obras:
            if o.get_atores() != None:
                atores = o.get_atores().split(", ")
                for ator in atores:
                    ator = ator.strip()
                    if ator in atores_count:
                        atores_count[ator] += 1
                    else:
                        atores_count[ator] = 1
        
        if atores:
            atores_ordenados = sorted(atores_count.items(), key=lambda x: x[1], reverse=True)

            mais_aparecem = atores_ordenados[:3]
            menos_aparecem = atores_ordenados[-3:]
            
            print("3 atores que mais aaprecem:")
            file.write("3 atores que mais aparecem:\n")
            for ator, qtd in mais_aparecem:
                print(f" - {ator}: {qtd}")
                file.write(f" - {ator}: {qtd}\n")

            print("3 atores que menos aparecem:")
            file.write("3 atores que menos aparecem:\n")
            for ator, qtd in menos_aparecem:
                print(f" - {ator}: {qtd}")
                file.write(f" - {ator}: {qtd}\n")
            
        #O diretor com mais filmes no dataset.
        diretores_count = {}
        
        for o in Obras:
            if o.get_diretor() != None:
                diretores = o.get_diretor().split(", ")
                for diretor in diretores:
                    diretor = diretor.strip()
                    if diretor in diretores_count:
                        diretores_count[diretor] += 1
                    else:
                        diretores_count[diretor] = 1
        
        if diretores_count:
            diretores_ordenados = sorted(diretores_count.items(), key=lambda x: x[1], reverse=True)
            
        diretor_top, qtd_top = diretores_ordenados[0]
        print(f"Diretor com mais filmes: {diretor_top} ({qtd_top} filmes)")
        file.write(f"Diretor com mais filmes: {diretor_top} ({qtd_top} filmes)\n\n")
        
        #O diretor com o filme mais popular no IMDB (considerando a maior nota IMDB).
        
        top_nota = None
        top_filme = None
        top_diretor = None

        for f in Filmes:
            nota = f.get_imdb_rating()
            if nota is None:
                continue
            if top_nota is None or float(nota) > float(top_nota):
                top_nota = nota
                top_filme = f.get_titulo()
                top_diretor = f.get_diretor()
        
        print(f"Diretor com o filme mais popular no IMDB: {top_diretor} (Filme: {top_filme}, Nota: {top_nota})")
        file.write(f"Diretor com o filme mais popular no IMDB: {top_diretor} (Filme: {top_filme}, Nota: {top_nota})\n\n")
        
        #O diretor com o filme mais popular no Metascore (considerando a maior nota Metascore).
        
        top_nota = None
        top_filme = None
        top_diretor = None

        for f in Filmes:
            nota = f.get_metascore()
            if nota is None:
                continue
            if top_nota is None or float(nota) > float(top_nota):
                top_nota = nota
                top_filme = f.get_titulo()
                top_diretor = f.get_diretor()
        
        print(f"Diretor com o filme mais popular no Metascore: {top_diretor} (Filme: {top_filme}, Nota: {top_nota})")
        file.write(f"Diretor com o filme mais popular no Metascore: {top_diretor} (Filme: {top_filme}, Nota: {top_nota})\n\n")
        
        #O ano em que mais filmes foram lançados.
        
        anos_count = {}

        for f in Filmes:
            ano = f.get_ano()
            if ano is None:
                continue
            if ano in anos_count:
                anos_count[ano] += 1
            else:
                anos_count[ano] = 1

        if anos_count:
            max_qtd = max(anos_count.values())
            anos_top = [ano for ano, qtd in anos_count.items() if qtd == max_qtd]

            print(f"Ano com mais filmes lançados: {anos_top[0]}: {max_qtd} filmes")
            file.write(f"Ano com mais filmes lançados: {anos_top[0]}: {max_qtd} filmes\n\n")

        #A pior série segundo a nota IMDB 
        
        pior_nota = None
        pior_serie = None
        
        for s in Series:
            nota = s.get_imdb_rating()
            if nota is None:
                continue
            if pior_nota is None or float(nota) < float(pior_nota):
                pior_nota = nota
                pior_serie = s.get_titulo()
        
        print(f"Pior série segundo a nota IMDB: {pior_serie} (Nota: {pior_nota})")
        file.write(f"Pior série segundo a nota IMDB: {pior_serie} (Nota: {pior_nota})\n\n")
        
        #A pior série segundo a nota Metascore
        
        pior_nota = None
        pior_serie = None
        
        for s in Series:
            nota = str(s.get_metascore()).strip().replace(',', '').replace('.', '')
            #print(s.titulo, s.get_metascore())
            if nota is None or nota == "None":
                continue
            if pior_nota is None or float(nota) < float(pior_nota):
                pior_nota = nota
                pior_serie = s.get_titulo()
        
        if pior_serie is None:
            print("Nenhuma série possui nota Metascore.")
            file.write("Nenhuma série possui nota Metascore.\n\n")
        else:
            print(f"Pior série segundo a nota Metascore: {pior_serie} (Nota: {pior_nota})")
            file.write(f"Pior série segundo a nota Metascore: {pior_serie} (Nota: {pior_nota})\n\n")
        
        #Uma lista de filmes que possuem mais de um lançamento (considerados "remakes" ou 
        #diferentes versões no dataset, identificados por títulos iguais mas anos de lançamento diferentes).
        
        titulosAnos = {}

        for f in Filmes:
            titulo = f.get_titulo()
            ano = f.get_ano()
            if not titulo or ano is None:
                continue

        #titulo = " ".join(titulo.split()).casefold()

        if titulo not in titulosAnos:
            titulosAnos[titulo] = {"titulo": titulo, "anos": set()}
        titulosAnos[titulo]["anos"].add(ano)
        
        remakes = [(v["titulo"], sorted(v["anos"])) for v in titulosAnos.values() if len(v["anos"]) > 1]

        remakes.sort(key=lambda x: (x[0].lower(), x[1]))

        if remakes:
            print("Filmes com múltiplos lançamentos:")
            file.write("Filmes com múltiplos lançamentos:\n")
            for titulo, anos in remakes:
                print(f" - {titulo}: {', '.join(str(a) for a in anos)}")
                file.write(f" - {titulo}: {', '.join(str(a) for a in anos)}\n")
        else:
            print("Nenhum filme com múltiplos lançamentos encontrado.")
            file.write("Nenhum filme com múltiplos lançamentos encontrado.\n")
        #O relatório de saída deve ser salvo em um arquivo texto chamado relatorio-disney.txt no mesmo diretório do script.
    file.close()
    
Obras = []
Obras = abrir_filmes_disney()

gerar_relatorio(Obras)
