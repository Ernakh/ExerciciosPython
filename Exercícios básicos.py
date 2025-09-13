#Atividade 1: Classificar Nota
#Crie uma variável nota_final e atribua um valor numérico a ela.
#Use uma estrutura condicional (if/elif/else) para verificar a nota e imprimir a classificação do aluno:
#Se a nota for maior ou igual a 7, imprima "Aprovado".
#Se a nota for maior ou igual a 5 e menor que 7, imprima "Recuperação".
#Caso contrário, imprima "Reprovado".

nota_final = 7.5;

if nota_final >= 7:
    print("Aprovado");
elif nota_final >= 5:
    print("Recuperação");
else:
    print("Reprovado");


#Atividade 2: Processando lista de frutas
#Crie uma lista chamada frutas com pelo menos 5 nomes de frutas.
#Use um laço de repetição for para iterar sobre a lista.
#Dentro do loop, use uma condicional (if) para verificar se o nome da fruta é "morango".
#Se for "morango", imprima "Eu amo morangos!". Se não for, imprima o nome da fruta.

frutas = ["banana", "maçã", "morango", "uva", "laranja"];

for fruta in frutas:
  if fruta == "morango":
    print("Eu amo morangos!");  
  else:
    print(fruta);


#Atividade 3: Contar Vogais em uma Frase
#Crie uma variável frase e atribua a ela uma frase de sua escolha.
#Crie uma variável contador_vogais e inicialize-a com 0.
#Defina uma lista ou string com todas as vogais (vogais = "aeiouAEIOU").
#Use um laço de repetição for para percorrer cada caractere da frase.
#Dentro do loop, use uma condicional (if) para verificar se o caractere atual está presente na lista de vogais.
#Se estiver, incremente contador_vogais em 1.
#Após o loop, imprima a frase e o total de vogais encontradas.

frase = "Grêmio Campeão do mundo!";
contador_vogais = 0;
vogais = "aeiouAEIOU";

for caractere in frase:
    if caractere in vogais:
        contador_vogais += 1

print("Frase:", frase)
print("Total de vogais encontradas:", contador_vogais)


#Atividade 4: Criar um Dicionário de Produtos
#Crie um dicionário chamado produtos onde as chaves são os nomes dos produtos e os valores são outros dicionários com as chaves "preço" e "em_estoque" (com valores numéricos e booleanos, respectivamente). Adicione pelo menos 3 produtos.
#Exemplo: {'camiseta': {'preço': 50, 'em_estoque': True}}
#Use um laço de repetição for para percorrer os itens do dicionário de produtos.
#Dentro do loop, imprima o nome do produto e seu preço.
#Adicione uma condicional (if) para verificar se o produto está em estoque. Se não estiver, imprima "Produto fora de estoque".

produtos = {
    "camiseta": {"preço": 50, "em_estoque": True},
    "calça": {"preço": 120, "em_estoque": False},
    "tênis": {"preço": 200, "em_estoque": True}
};

for produto, detalhes in produtos.items():
    print(f"Produto: {produto} | Preço: R$ {detalhes['preço']}");
    
    if not detalhes["em_estoque"]:
        print("Produto fora de estoque");

#Atividade 5: Análise de Vendas de Produtos
#Crie uma lista chamada registros_vendas, onde cada item da lista é um dicionário representando uma venda. Cada dicionário deve ter as chaves "produto", "quantidade" e "valor_unitario". Adicione pelo menos 5 registros de vendas.
#Crie uma variável vendas_totais e inicialize-a com 0.
#Crie uma variável produtos_mais_vendidos como um dicionário vazio.
#Use um laço de repetição for para percorrer a lista registros_vendas.
#Dentro do loop, calcule o valor total de cada venda (quantidade * valor_unitario) e adicione-o a vendas_totais.
#Use um condicional para verificar se o produto da venda já existe no dicionário produtos_mais_vendidos. Se sim, adicione a quantidade vendida. Se não, adicione o produto como uma nova chave com a quantidade atual.
#Após o loop, imprima o valor total de todas as vendas e o dicionário produtos_mais_vendidos para ver o total de unidades vendidas por produto.

registros_vendas = [
    {"produto": "camiseta", "quantidade": 3, "valor_unitario": 50},
    {"produto": "calça", "quantidade": 2, "valor_unitario": 120},
    {"produto": "tênis", "quantidade": 1, "valor_unitario": 200},
    {"produto": "camiseta", "quantidade": 2, "valor_unitario": 50},
    {"produto": "boné", "quantidade": 4, "valor_unitario": 30}
];

vendas_totais = 0;
produtos_mais_vendidos = {};

for venda in registros_vendas:
    valor_total = venda["quantidade"] * venda["valor_unitario"];
    vendas_totais += valor_total;
    
    produto = venda["produto"];

    if produto in produtos_mais_vendidos:
        produtos_mais_vendidos[produto] += venda["quantidade"];
    else:
        produtos_mais_vendidos[produto] = venda["quantidade"];

print("Valor total de todas as vendas: R$", vendas_totais);
print("Produtos mais vendidos (quantidade por produto):");
print(produtos_mais_vendidos);


#Atividade 1: Contar Frequência de Palavras
#Crie uma variável texto com uma frase de sua escolha.
#Crie um dicionário vazio chamado contagem_palavras.
#Separe a frase em palavras (dica: use o método .split()).
#Use um laço de repetição for para percorrer a lista de palavras.
#Dentro do loop, use um condicional (if/else) para verificar se a palavra já é uma chave no dicionário contagem_palavras.
#Se a palavra existir, incremente seu valor em 1.
#Se não existir, adicione a palavra como uma nova chave com o valor 1.
#Ao final, imprima o dicionário contagem_palavras.

texto = "Grêmio vai sair campeão! Vai sair campeão!";
contagem_palavras = {};
palavras = texto.split();

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1;
    else:
        contagem_palavras[palavra] = 1;
        
print("Contagem de palavras:", contagem_palavras);


#Atividade 2: Analisar Dados de Alunos
#Crie uma lista chamada alunos, onde cada item é um dicionário com as chaves "nome" e "nota". Adicione pelo menos 4 alunos.
#Crie uma variável soma_notas e inicialize-a com 0.
#Crie uma variável melhor_aluno como um dicionário vazio.
#Use um laço de repetição for para iterar sobre a lista alunos.
#Dentro do loop, adicione a nota de cada aluno à soma_notas.
#Use um condicional para verificar se a nota do aluno atual é maior que a nota armazenada em melhor_aluno. Se sim, atualize o dicionário melhor_aluno com os dados do aluno atual.
#Após o loop, calcule a média da turma (soma_notas dividida pelo número de alunos) e imprima o nome do aluno com a maior nota e a média da turma.

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.2},
    {"nome": "Diego", "nota": 7.5}
];

soma_notas = 0;
melhor_aluno = {"nome": "", "nota": 0};

for aluno in alunos:
    soma_notas += aluno["nota"];
    
    if aluno["nota"] > melhor_aluno["nota"]:
        melhor_aluno = aluno;

media_turma = soma_notas / len(alunos);

print("Melhor aluno:", melhor_aluno["nome"], "com nota", melhor_aluno["nota"]);
print("Média da turma:", media_turma);


#Atividade 3: Gerar um Tabuleiro de Xadrez
#Crie uma lista vazia chamada tabuleiro.
#Use um laço de repetição for externo para iterar 8 vezes (representando as linhas).
#Dentro dele, crie uma lista vazia chamada linha.
#Use um laço de repetição for interno para iterar 8 vezes (representando as colunas).
#Dentro do loop interno, use um condicional para adicionar uma string que representa a cor da casa ('preto' ou 'branco') à linha, alternando a cor a cada passo.
#Adicione a linha completa ao tabuleiro após o loop interno.
#Imprima o tabuleiro completo.

tabuleiro = [];

for i in range(8):
    linha = [];
    for j in range(8):
        if (i + j) % 2 == 0:
            linha.append("branco");
        else:
            linha.append("preto");
    tabuleiro.append(linha);

for linha in tabuleiro:
    print(linha);


#Atividade 4: Análise de Dados de Sensores
#Crie uma lista de dicionários chamada leituras_sensores, onde cada dicionário tem as chaves "sensor_id", "valor" (numérico) e "data" (string). Adicione pelo menos 5 leituras.
#Crie variáveis para a soma dos valores, o maior valor, o menor valor e a contagem de leituras.
#Crie um dicionário vazio chamado alertas para armazenar leituras com valor acima de um limite (por exemplo, 30).
#Use um laço de repetição for para percorrer a lista leituras_sensores.
#Dentro do loop, atualize as variáveis de soma, maior e menor valor.
#Use um condicional (if) para verificar se o valor da leitura é maior que o limite. Se sim, adicione a leitura completa ao dicionário alertas com o sensor_id como chave.
#Após o loop, calcule a média dos valores e imprima um relatório com o valor médio, o maior valor, o menor valor e o dicionário alertas com as leituras que ultrapassaram o limite.

leituras_sensores = [
    {"sensor_id": "S1", "valor": 25, "data": "2025-09-01"},
    {"sensor_id": "S2", "valor": 32, "data": "2025-09-02"},
    {"sensor_id": "S3", "valor": 28, "data": "2025-09-03"},
    {"sensor_id": "S4", "valor": 40, "data": "2025-09-04"},
    {"sensor_id": "S5", "valor": 18, "data": "2025-09-05"}
];

soma_valores = 0;
maior_valor = float("-inf");
menor_valor = float("inf");
contagem = 0;
alertas = {};

limite = 30;

for leitura in leituras_sensores:
    valor = leitura["valor"];
    soma_valores += valor;
    contagem += 1;

    if valor > maior_valor:
        maior_valor = valor;
    if valor < menor_valor:
        menor_valor = valor;

    if valor > limite:
        alertas[leitura["sensor_id"]] = leitura;

media_valores = soma_valores / contagem;

print("Relatório de Análise de Sensores");
print("Valor médio:", media_valores);
print("Maior valor:", maior_valor);
print("Menor valor:", menor_valor);
print("Alertas (leituras acima do limite):");
print(alertas);

#Atividade 5: Consolidação e Limpeza de Dados de Múltiplas Fontes
#Crie duas listas de dicionários, sensores_leste e sensores_oeste, cada uma com pelo menos 3 dicionários. Cada dicionário deve ter as chaves "id", "temperatura" (numérico) e "umidade" (numérico). Inclua valores negativos ou nulos para simular dados inválidos.
#Crie uma lista vazia chamada dados_validos.
#Use loops de repetição para percorrer as duas listas de sensores. Dentro dos loops, use condicionais (if) para verificar se os valores de "temperatura" e "umidade" são positivos.
#Se os dados forem válidos, adicione o dicionário completo à lista dados_validos.
#Após os loops, use um laço for para iterar sobre a lista dados_validos. Calcule e armazene a temperatura média, a umidade média, a temperatura máxima e a umidade máxima.
#Use um dicionário para contar o número de leituras válidas de cada sensor (usando o "id" como chave).
#Imprima um relatório final com as médias, os valores máximos e a contagem de leituras por sensor.

sensores_leste = [
    {"id": "L1", "temperatura": 25.2, "umidade": 60.1},
    {"id": "L2", "temperatura": -3.0, "umidade": 55.0},
    {"id": "L3", "temperatura": 22.8, "umidade": None}    
];
sensores_oeste = [
    {"id": "O1", "temperatura": 27.5, "umidade": 58.0},
    {"id": "O2", "temperatura": 0, "umidade": 49.0},    
    {"id": "O3", "temperatura": 26.1, "umidade": 61.2}
];

dados_validos = []

def leitura_valida(d):
    t, u = d.get("temperatura"), d.get("umidade");
    return (isinstance(t, (int, float)) and isinstance(u, (int, float)) and t > 0 and u > 0);
    
for leitura in sensores_leste:
    if leitura_valida(leitura):
        dados_validos.append(leitura);

for leitura in sensores_oeste:
    if leitura_valida(leitura):
        dados_validos.append(leitura);

if not dados_validos:
    print("Nenhuma leitura válida encontrada.");
else:
    soma_temp = 0.0;
    soma_umid = 0.0;
    temp_max = float("-inf");
    umid_max = float("-inf");
    contagem_por_sensor = {};

    for d in dados_validos:
        t = d["temperatura"];
        u = d["umidade"];
        soma_temp += t;
        soma_umid += u;
        if t > temp_max:
            temp_max = t;
        if u > umid_max:
            umid_max = u;

        sensor_id = d["id"];

        if sensor_id in contagem_por_sensor:
            contagem_por_sensor[sensor_id] += 1;
        else:
            contagem_por_sensor[sensor_id] = 1;

    n = len(dados_validos);
    temp_media = soma_temp / n;
    umid_media = soma_umid / n;

    print("Relatório");
    print(f"Leituras válidas: {n}");
    print(f"Temperatura média: {temp_media:.2f}°C");
    print(f"Umidade média: {umid_media:.2f}%");
    print(f"Temperatura máxima: {temp_max:.2f}°C");
    print(f"Umidade máxima: {umid_max:.2f}%");
    print("Contagem de leituras por sensor:");

    for sid, cnt in contagem_por_sensor.items():
        print(f"  - {sid}: {cnt}");
