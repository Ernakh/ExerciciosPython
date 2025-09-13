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
