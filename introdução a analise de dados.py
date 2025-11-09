import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('expectancy.csv')
    print("Arquivo lido com sucesso!")
except FileNotFoundError:
    print("ERRO: O arquivo 'expectancy.csv' não foi encontrado. Verifique o caminho/diretório.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")



df.info()

df.head(5)

df.tail(5)

df.describe()

df.isnull().sum()

# 1 - Quantas linhas e colunas temos no nosso dataset?
print(f"O dataset possui {df.shape[0]} linhas")
print(f"O dataset possui {df.shape[1]} colunas")

# 2 - Temos dados nulos? Se sim, qual a porcentagem deles? É uma porcentagem significativa?
#percentagem = (df.isnull().sum().sum() / len(df)) * 100;
#print(f"Porcentagem Nulos (%): {percentagem.round(2)}");

percentagem = (df.isnull().sum() / len(df)) * 100;
print(f"Porcentagem Nulos (%): {percentagem.round(2)}");

# 3 - Sobre os dados nulos com maior porcentagem, qual o tipo deles? Tente pensar em hipóteses do porquê eles estão nulos.
print("--- 2. Análise de Dados Nulos e Porcentagem ---")
null_counts = df.isnull().sum()
null_percentages = (null_counts / len(df)) * 100
null_data = pd.DataFrame({
    'Contagem Nulos': null_counts,
    'Porcentagem Nulos (%)': null_percentages.round(2)
}).sort_values(by='Porcentagem Nulos (%)', ascending=False)

null_data_filtered = null_data[null_data['Contagem Nulos'] > 0]
print("Dados nulos por coluna:")
print(null_data_filtered)

if not null_data_filtered.empty:
    top_null_col = null_data_filtered.index[0]
    top_null_dtype = df[top_null_col].dtype
    top_null_perc = null_data_filtered.iloc[0]['Porcentagem Nulos (%)']
    
    # 3. Sobre os dados nulos com maior porcentagem
    print("\n--- 3. Detalhes sobre a Coluna com Mais Nulos ---")
    print(f"Coluna com maior porcentagem de nulos: '{top_null_col}'")
    print(f"Tipo de dados da coluna: {top_null_dtype}")
    
    # Avaliação da significância: Acima de 10-15% já é considerado significativo para imputação ou remoção.
    print(f"Porcentagem de Nulos: {top_null_perc:.2f}%")
    if top_null_perc > 15:
        print("É uma porcentagem **significativa**.")
    elif top_null_perc > 5:
        print("É uma porcentagem **moderada**.")
    else:
        print("É uma porcentagem **baixa**.")
        
    # Hipótese (Exemplo de coluna que é comum em datasets de expectativa de vida)
    print("\n--- Hipótese do Porquê Estão Nulos ---")
    print(f"Se '{top_null_col}' for 'GDP' (PIB) ou 'Hepatitis B' (Vacinação), é comum que dados de países menos desenvolvidos ou anos mais antigos estejam faltando devido a **falta de coleta** ou **registro incompleto**.")
    print("O tipo de dado sendo 'float' ou 'int' (numérico) é comum para dados ausentes (NaN).")
    
print("\n" + "="*50 + "\n")

#v2

# -----------------------------
# 1. Verificar quantidade e porcentagem de valores nulos
# -----------------------------
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100
missing_data = pd.DataFrame({
    'Valores Nulos': missing_count,
    'Percentual (%)': missing_percent
}).sort_values(by='Percentual (%)', ascending=False)

print(">>> Tabela de valores nulos por coluna:")
print(missing_data)

# -----------------------------
# 2. Visualizar graficamente os dados nulos
# -----------------------------
plt.figure(figsize=(12,6))
sns.barplot(
    x=missing_data.index,
    y=missing_data['Percentual (%)'],
    palette='viridis'
)
plt.xticks(rotation=90)
plt.title('Percentual de Valores Nulos por Coluna', fontsize=14)
plt.ylabel('Percentual (%)')
plt.xlabel('Colunas')
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Heatmap de dados nulos (para ver padrões por linha)
# -----------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='mako', yticklabels=False)
plt.title('Mapa de Dados Nulos no Dataset')
plt.show()

# -----------------------------
# 4. Exemplo de inspeção de uma coluna com nulos
# -----------------------------
coluna_nula = missing_data.index[0]  # Pega a coluna com mais nulos
print(f"\n>>> Coluna com mais valores nulos: {coluna_nula}")
print(f"Média: {df[coluna_nula].mean()}")
print(f"Mediana: {df[coluna_nula].median()}")
print(f"Moda: {df[coluna_nula].mode()[0]}")

# -----------------------------
# 5. Insight orientativo
# -----------------------------
print("""
Interpretação sugerida:
As colunas com maior percentual de nulos geralmente estão relacionadas a fatores
econômicos e demográficos, como 'Population' e 'GDP'. Isso pode indicar ausência
de registros em países menores ou com sistemas de coleta de dados frágeis,
especialmente entre países em desenvolvimento.
""")


# 4 - Existem duplicatas?

duplicatas = df.duplicated()
num_duplicatas = duplicatas.sum()

print(f"Total de linhas duplicadas: {num_duplicatas}")

if num_duplicatas > 0:
    print("\nLinhas duplicadas encontradas:")
    print(df[duplicatas].head()) 
else:
    print("Não há linhas duplicadas no dataset.")

# 5 - Todas as colunas estão com o seu tipo correto?
#Não, algumas colunas que deveriam ser numéricas estão como objetos.

# 6 - Como verificar as principais estatísticas das colunas numéricas? Escolha uma coluna com valores nulos para verificar como a média, moda, mediana.

nulos_population = df['Population'].isnull().sum()
print(f"Valores nulos em 'Population': {nulos_population}")

# -----------------------------
# 2. Calcular média, mediana e moda
# -----------------------------
media = df['Population'].mean()
mediana = df['Population'].median()
moda = df['Population'].mode()[0]

print("\n>>> Estatísticas da coluna 'Population':")
print(f"Média: {media:,.2f}")
print(f"Mediana: {mediana:,.2f}")
print(f"Moda: {moda:,.2f}")

# -----------------------------
# 3. Estatísticas descritivas gerais (para complementar)
# -----------------------------
print("\n>>> Estatísticas descritivas gerais:")
print(df['Population'].describe())


#Análise Univariada
# 7 -Como as variáveis numéricas estão distribuídas? Alguma apresenta distribuição normal, ou todas são assimétricas?

# -----------------------------
# 1. Selecionar apenas colunas numéricas
# -----------------------------
df_num = df.select_dtypes(include=['float64', 'int64'])

# -----------------------------
# 2. Calcular a assimetria (skewness)
# -----------------------------
skewness = df_num.skew().sort_values(ascending=False)
print(">>> Assimetria (Skewness) das variáveis numéricas:\n")
print(skewness)

# -----------------------------
# 3. Gráfico de barras com os valores de skewness
# -----------------------------
plt.figure(figsize=(12,6))
sns.barplot(x=skewness.index, y=skewness.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('Assimetria (Skewness) das Variáveis Numéricas', fontsize=14)
plt.ylabel('Skewness')
plt.xlabel('Variáveis')
plt.axhline(0, color='black', linestyle='--')
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Visualizar algumas distribuições principais
# -----------------------------
colunas_exemplo = ['Life expectancy', 'Adult Mortality', 'BMI', 'GDP', 'Population']

plt.figure(figsize=(14,8))
for i, col in enumerate(colunas_exemplo, 1):
    plt.subplot(2, 3, i)
    sns.histplot(df[col], kde=True, color='skyblue')
    plt.title(col)
plt.tight_layout()
plt.show()

# 8 - Qual país aparece com maior frequência? E o menos frequente?

frequencia_paises = df['Country'].value_counts()

# Utilizo o Idx para ver a manior e menor incidência de países
pais_mais_frequente = frequencia_paises.idxmax()
pais_menos_frequente = frequencia_paises.idxmin()

print(f"País que aparece com maior frequência: {pais_mais_frequente} ({frequencia_paises.max()} vezes)")
print(f"País que aparece com menor frequência: {pais_menos_frequente} ({frequencia_paises.min()} vez(es))")

# 9 - Existem mais países em desenvolvimento ou desenvolvidos?

contagem_status = df['Status'].value_counts().reset_index()
contagem_status.columns = ['Status', 'Frequência']

plt.figure(figsize=(8, 6))

ax = sns.barplot(
    x='Status',
    y='Frequência',
    data=contagem_status,
    palette='viridis',
    hue='Status' # Corrigindo o warning de depreciação
)

# Adicionar Rótulos de Dados (Frequência)
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f')

plt.title('Frequência de Países por Status (Desenvolvido vs. Em Desenvolvimento)', fontsize=14)
plt.xlabel('Status', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.xticks(rotation=0)

# Ocultar a legenda (Correção alternativa ao erro)
if ax.legend_:
    ax.legend_.remove()

plt.tight_layout()
plt.show()

print("\n EXISTEM MAIS PAÍSES EM DESENVOLVIMENTO")

# 10 - Os outliers existentes são reais ou valores extremos que não condizem com a realidade?

# 1. Identificar Colunas Numéricas
# Excluímos 'Year' (ano) e 'Unnamed: 0' (índice) se for o caso, pois são identificadores, não variáveis para análise de outlier.
colunas_numericas = df.select_dtypes(include=['number']).columns.tolist()
colunas_para_plot = [col for col in colunas_numericas if col not in ['Year', 'Unnamed: 0']]

# 2. Configurar o layout de múltiplos gráficos
# Define quantos gráficos por linha e coluna teremos
n_cols = 3
n_rows = (len(colunas_para_plot) + n_cols - 1) // n_cols # Cálculo para garantir linhas suficientes

plt.figure(figsize=(18, 5 * n_rows)) # Ajusta o tamanho da figura

# 3. Gerar Boxplots para cada coluna
for i, col in enumerate(colunas_para_plot):
    plt.subplot(n_rows, n_cols, i + 1) # Cria o subplot na posição correta
    
    # Remove NaNs apenas para plotagem, para garantir que o boxplot funcione
    data_plot = df[col].dropna()

    # Aplica escala logarítmica para variáveis com grande dispersão (como GDP e População)
    if col in ['GDP', 'Population', 'percentage expenditure']:
        # Adicionamos um pequeno valor (1) para evitar log(0), caso haja zeros
        sns.boxplot(y=data_plot, color='skyblue')
        plt.yscale('log')
        plt.title(f'Boxplot de {col} (Escala Log)', fontsize=14)
    else:
        sns.boxplot(y=data_plot, color='lightcoral')
        plt.title(f'Boxplot de {col}', fontsize=14)
    
    plt.ylabel(col)

plt.tight_layout() # Ajusta automaticamente os subplots para que não haja sobreposição
plt.show()

# 11 - Qual o ano que apresenta mais informações?

# Conto quantas vezes cada ano aparece
frequencia_anos = df['Year'].value_counts()

# Exibo o ano com mais informações
ano_com_mais_info = frequencia_anos.idxmax()
qtd = frequencia_anos.max()

print(f"O ano que apresenta mais informações é {ano_com_mais_info}, com {qtd} registros.")

# 12 - Como está a escolaridade média?

print(">>> Estatísticas da coluna 'Schooling':")
print(df['Schooling'].describe())

media_escolaridade = df['Schooling'].mean()
print(f"\nEscolaridade média global: {media_escolaridade:.2f} anos")

# -----------------------------
# 2. Escolaridade média por status de país
# -----------------------------
media_por_status = df.groupby('Status')['Schooling'].mean().sort_values(ascending=False)
print("\n>>> Escolaridade média por tipo de país:")
print(media_por_status)

# Gráfico comparando países desenvolvidos x em desenvolvimento
plt.figure(figsize=(6,4))
sns.barplot(x=media_por_status.index, y=media_por_status.values, palette='viridis')
plt.title('Escolaridade Média por Tipo de País', fontsize=13)
plt.ylabel('Anos Médios de Escolaridade')
plt.xlabel('Status do País')
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Evolução da escolaridade ao longo dos anos
# -----------------------------
# Converter ano para numérico (caso ainda esteja como texto)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

escolaridade_por_ano = df.groupby('Year')['Schooling'].mean()

plt.figure(figsize=(10,5))
sns.lineplot(x=escolaridade_por_ano.index, y=escolaridade_por_ano.values, marker='o')
plt.title('Evolução da Escolaridade Média (2000–2015)')
plt.xlabel('Ano')
plt.ylabel('Anos Médios de Escolaridade')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#3. Análise Bivariada

# 13 - Países mais ricos vivem mais?

df_gdp = df[['Country', 'Status', 'GDP', 'Life expectancy']].dropna()

# -----------------------------
# 2. Estatísticas básicas
# -----------------------------
print(">>> Estatísticas descritivas das variáveis analisadas:")
print(df_gdp[['GDP', 'Life expectancy']].describe())

# -----------------------------
# 3. Correlação entre PIB e Expectativa de Vida
# -----------------------------
correlacao = df_gdp['GDP'].corr(df_gdp['Life expectancy'])
print(f"\nCoeficiente de correlação (Pearson) = {correlacao:.3f}")

if correlacao > 0.7:
    interpretacao = "Correlação forte e positiva"
elif correlacao > 0.4:
    interpretacao = "Correlação moderada e positiva"
elif correlacao > 0.2:
    interpretacao = "Correlação fraca e positiva"
else:
    interpretacao = "Correlação muito fraca ou inexistente"

print(f"Interpretação: {interpretacao}")

# -----------------------------
# 4. Gráfico de dispersão com linha de tendência
# -----------------------------
plt.figure(figsize=(8,6))
sns.regplot(
    x='GDP', 
    y='Life expectancy', 
    data=df_gdp,
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'}
)
plt.title('Relação entre PIB per capita e Expectativa de Vida', fontsize=13)
plt.xlabel('PIB per capita (USD)')
plt.ylabel('Expectativa de Vida (anos)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Comparação por Status de Desenvolvimento
# -----------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    x='GDP', 
    y='Life expectancy', 
    hue='Status',
    data=df_gdp,
    alpha=0.7
)
plt.title('PIB x Expectativa de Vida (por Status de Desenvolvimento)', fontsize=13)
plt.xlabel('PIB per capita (USD)')
plt.ylabel('Expectativa de Vida (anos)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Status do País')
plt.tight_layout()
plt.show()


# 14 - O nível de escolaridade influencia a expectativa de vida?

df_corr = df[['Schooling', 'Life expectancy']].dropna()
print(df_corr.describe())

correlacao = df_corr['Schooling'].corr(df_corr['Life expectancy'])
print(f"\nCoeficiente de correlação (Pearson) = {correlacao:.3f}")

# Interpretação
if correlacao > 0.7:
    interpretacao = "Correlação forte e positiva"
elif correlacao > 0.4:
    interpretacao = "Correlação moderada e positiva"
elif correlacao > 0.2:
    interpretacao = "Correlação fraca e positiva"
elif correlacao < -0.2:
    interpretacao = "Correlação negativa"
else:
    interpretacao = "Correlação muito fraca ou inexistente"

print(f"Interpretação: {interpretacao}")


# 15 - Países desenvolvidos consomem mais álcool?
df_alcohol = df[['Country', 'Status', 'Alcohol']].dropna()


print(">>> Consumo médio de álcool por Status de desenvolvimento:\n")
print(df_alcohol.groupby('Status')['Alcohol'].describe())

mean_dev = df_alcohol[df_alcohol['Status'] == 'Developed']['Alcohol'].mean()
mean_devp = df_alcohol[df_alcohol['Status'] == 'Developing']['Alcohol'].mean()

print(f"\nMédia (Developed): {mean_dev:.2f} litros por pessoa/ano")
print(f"Média (Developing): {mean_devp:.2f} litros por pessoa/ano")

if mean_dev > mean_devp:
    print("➡️ Países desenvolvidos consomem mais álcool, em média.")
else:
    print("➡️ Países em desenvolvimento consomem mais álcool, em média.")

# 16 - A mortalidade infantil ainda é um problema em países em desenvolvimento?
df_infant = df[['Country', 'Status', 'infant deaths', 'Year']].dropna()

# -----------------------------
# 2. Estatísticas descritivas por Status
# -----------------------------
print(">>> Estatísticas descritivas da mortalidade infantil por Status:\n")
print(df_infant.groupby('Status')['infant deaths'].describe())

# -----------------------------
# 3. Médias comparativas
# -----------------------------
mean_dev = df_infant[df_infant['Status'] == 'Developed']['infant deaths'].mean()
mean_devp = df_infant[df_infant['Status'] == 'Developing']['infant deaths'].mean()

print(f"\nMédia (Developed): {mean_dev:.2f} mortes por 1.000 habitantes")
print(f"Média (Developing): {mean_devp:.2f} mortes por 1.000 habitantes")

if mean_devp > mean_dev:
    print("➡️ A mortalidade infantil é significativamente maior em países em desenvolvimento.")
else:
    print("➡️ A mortalidade infantil é semelhante ou maior em países desenvolvidos (raro).")

# 17 - Como a expectativa de vida evoluiu ao longo do tempo?
df['Year'] = df['Year'].astype(str).str.replace('O', '0').str.replace('o', '0')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')  # converte para número, ignora inválidos

# -----------------------------
# 3. Selecionar colunas e remover valores nulos
# -----------------------------
df_life = df[['Country', 'Year', 'Status', 'Life expectancy']].dropna(subset=['Life expectancy', 'Year'])
df_life = df_life.sort_values('Year')

# -----------------------------
# 4. Expectativa de vida média global por ano
# -----------------------------
vida_media_ano = df_life.groupby('Year', as_index=False)['Life expectancy'].mean()

print(">>> Expectativa de vida média global por ano (parcial):")
print(vida_media_ano.head())

# -----------------------------
# 5. Gráfico global (ordenado)
# -----------------------------
plt.figure(figsize=(10,6))
sns.lineplot(
    data=vida_media_ano,
    x='Year',
    y='Life expectancy',
    marker='o',
    color='tab:blue'
)
plt.title('Evolução Global da Expectativa de Vida (2000–2015)', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida Média (anos)')
plt.xticks(sorted(df_life['Year'].unique()))
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# -----------------------------
# 6. Expectativa de vida média por Status
# -----------------------------
vida_media_status = df_life.groupby(['Year', 'Status'], as_index=False)['Life expectancy'].mean()

plt.figure(figsize=(10,6))
sns.lineplot(
    data=vida_media_status,
    x='Year',
    y='Life expectancy',
    hue='Status',
    marker='o',
    palette='husl'
)
plt.title('Evolução da Expectativa de Vida por Status de Desenvolvimento (2000–2015)', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida Média (anos)')
plt.xticks(sorted(df_life['Year'].unique()))
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# -----------------------------
# 7. Estatísticas comparativas (2000 x 2015)
# -----------------------------
vida_2000 = vida_media_status[vida_media_status['Year'] == 2000]
vida_2015 = vida_media_status[vida_media_status['Year'] == 2015]

print("\n>>> Expectativa de vida média em 2000 e 2015 por Status:")
print(pd.concat([vida_2000, vida_2015]))

# -----------------------------
# 8. Interpretação
# -----------------------------
print("""
Interpretação:
- Agora o erro '2O15' foi corrigido automaticamente.
- Os gráficos mostram aumento constante da expectativa de vida entre 2000 e 2015.
- Países desenvolvidos mantêm médias mais altas (~80 anos),
  enquanto países em desenvolvimento aumentam de ~60 para ~68 anos.
- A diferença diminui ao longo do tempo, refletindo avanços em saúde e qualidade de vida.
""")

# 18 - Países com maior investimento em saúde têm maior expectativa de vida?
df['Year'] = df['Year'].astype(str).str.replace('O', '0').str.replace('o', '0')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# -----------------------------
# 2. Selecionar colunas relevantes e remover valores nulos
# -----------------------------
df_health = df[['Country', 'Status', 'Year', 'Life expectancy', 'Total expenditure']].dropna(subset=['Life expectancy', 'Total expenditure'])

# -----------------------------
# 3. Visualizar a relação entre investimento e expectativa de vida
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df_health,
    x='Total expenditure',
    y='Life expectancy',
    hue='Status',
    alpha=0.7,
    s=60,
    palette='Set1'
)
sns.regplot(
    data=df_health,
    x='Total expenditure',
    y='Life expectancy',
    scatter=False,
    color='black',
    line_kws={'lw':2, 'ls':'--'}
)
plt.title('Investimento em Saúde x Expectativa de Vida', fontsize=14)
plt.xlabel('Total expenditure (% do PIB em saúde)')
plt.ylabel('Expectativa de Vida (anos)')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Correlação
# -----------------------------
correlacao = df_health['Life expectancy'].corr(df_health['Total expenditure'])
print(f"Correlação entre investimento em saúde e expectativa de vida: {correlacao:.3f}")

# -----------------------------
# 5. Interpretação
# -----------------------------
if correlacao > 0.5:
    interpretacao = "forte correlação positiva"
elif correlacao > 0.3:
    interpretacao = "correlação moderada positiva"
elif correlacao > 0.1:
    interpretacao = "correlação fraca positiva"
else:
    interpretacao = "pouca ou nenhuma correlação"

print(f"""
>>> Interpretação:
A correlação calculada é de {correlacao:.3f}, indicando {interpretacao}.
Isso significa que, em geral, quanto maior o investimento em saúde (% do PIB),
maior tende a ser a expectativa de vida da população.

O gráfico reforça isso visualmente — países desenvolvidos (em vermelho) 
costumam investir mais em saúde e apresentam maiores médias de expectativa de vida.
""")


#4. Processamento dos Dados
#Nesta etapa, é necessário que você:

#Faça a limpeza das colunas erradas;
#Faça o tratamento dos valores nulos da forma que achar válido;
#Trate as duplicatas;
#Transforme as colunas categóricas em numéricas;
#Faça o escalonamento de variáveis numéricas;

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('expectancy.csv')
    print("Arquivo lido com sucesso!")
except FileNotFoundError:
    print("ERRO: O arquivo 'expectancy.csv' não foi encontrado. Verifique o caminho/diretório.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

print("Dimensões iniciais:", df.shape)
print("Colunas:", list(df.columns))
print("\nAmostra dos dados:")
print(df.head())

#4. Processamento dos Dados
#Nesta etapa, é necessário que você:
# - Faça a limpeza das colunas erradas;

## Corrigir erro na coluna 'Year'
df['Year'] = df['Year'].astype(str).str.replace('O', '0').str.replace('o', '0')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

##Padronizar nome das colunas (sem espaços e minúsculas)
df.columns = df.columns.str.strip().str.lower().str.replace('  ', '_').str.replace(' ', '_')
print("\nColunas após limpeza:", list(df.columns))

# - Faça o tratamento dos valores nulos da forma que achar válido;

print("\nPercentual de valores nulos por coluna:")
print((df.isnull().mean() * 100).round(2))

#percorre e substitui os nulos
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nValores nulos após tratamento:", df.isnull().sum().sum())

# - Trate as duplicatas;

duplicatas = df.duplicated().sum()
print(f"\nDuplicatas antes da remoção: {duplicatas}")
df.drop_duplicates(inplace=True)
print(f"Duplicatas após remoção: {df.duplicated().sum()}")


# - Transforme as colunas categóricas em numéricas;

cat_cols = df.select_dtypes(include=['object']).columns
print("\nColunas categóricas:", list(cat_cols))

# Exemplo: "Developing" -> 0, "Developed" -> 1
for col in cat_cols:
    df[col] = df[col].astype('category').cat.codes

print("\nTransformação concluída. Amostra dos dados numéricos:")
print(df.head())

# - Faça o escalonamento de variáveis numéricas; 
# usei IA nessa parte

num_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Aplicar normalização Z-score: (x - média) / desvio padrão
for col in num_cols:
    media = df[col].mean()
    desvio = df[col].std()
    if desvio != 0:
        df[col] = (df[col] - media) / desvio
    else:
        df[col] = 0  # Evita divisão por zero

print("\nEscalonamento concluído. Amostra dos dados escalonados:")
print(df[num_cols].head())

print("\nDimensões finais do DataFrame:", df.shape)
print("Tipos de dados após processamento:")
print(df.dtypes)

#salvo o arquivo corrigido
#testei no VS, mas aqui no colab tbm funcionou e gerou o arquivo
df.to_csv('expectancy_processed_manual.csv', index=False)



#5. Feature Engineer
#É aqui que sua imaginação precisa fluir. 
# Crie de duas a três novas variáveis relacionando as variáveis já existentes e 
# explique como elas poderiam agregar na capacidade do modelo de prever expectativa de vida.


#Investimento relativo em saúde
df['investimento_saude'] = df['total_expenditure'] / (df['gdp'] + 1) * 1000  
# +1 evita divisão por zero
#  mostro os dados absolutos

# Índice de escolaridade ajustado à renda
df['escolaridade'] = df['schooling'] * df['income_composition_of_resources']

#print(df[['investimento_saude', 'escolaridade']].head())#uma amostragem para analsiar os dados visualemnte
print(df[['investimento_saude', 'escolaridade']])

#Caso 1 - Investimento relativo em saúde
#Mede o quanto um país investe em saúde em relação ao PIB.
# Pode ajudar a explicar a expectativa de vida, pois países que investem proporcionalmente mais tendem a ter sistemas de saúde melhores
# Valores mais altos (como 2238) representam países ricos ou que priorizam saúde
# Mas, valores baixos ou negativos podem representar países com baixo investimento ou com PIB muito alto em relação ao gasto (problema?)
# Talvez os valroes negaativos seja um problema nos dados os na minha formula

#Caso 2 - Índice de escolaridade ajustado à renda
#Combina o nível de escolaridade com a composição de renda. Representa um nível socioeconômico ajustado, associado ao bem-estar e à longevidade populacional
# Valores mais altos (próximos de 1) indicam países com boa escolaridade e boa distribuição de renda
# Valores baixos ou negativos indicam países com baixa escolaridade e/ou má distribuição de renda

#       investimento_saude  escolaridade
# 0            1953.032394      0.421379
# 1            1961.651383      0.452585
# 2            1912.096644      0.494090
# 3            2238.563257      0.540676
# 4            1853.112918      0.648216
# ...                  ...           ...
# 2938        -1594.159042     -0.007401
# 2939          325.904630      0.443292
# 2940          378.688531      0.323037
# 2941         -171.089001      0.721624
# 2942        -1209.706831      0.966451

#tentativa de escaolar os dados, para 0 ser a media global, valores positivos são acima da média e os valores negativos são abaixo da média

print("\nDados escalonados:")
df['investimento_saude_scaled'] = (df['investimento_saude'] - df['investimento_saude'].mean()) / df['investimento_saude'].std()
df['escolaridade_scaled'] = (df['escolaridade'] - df['escolaridade'].mean()) / df['escolaridade'].std()

print(df[['investimento_saude_scaled', 'escolaridade_scaled']])

# Dados escalonados:
#       investimento_saude_scaled  escolaridade_scaled
# 0                      1.377291            -0.264865
# 1                      1.383092            -0.242806
# 2                      1.349740            -0.213467
# 3                      1.569463            -0.180537
# 4                      1.310042            -0.104520
# ...                         ...                  ...
# 2938                  -1.010085            -0.567958
# 2939                   0.282181            -0.249375
# ...
# 2941                  -0.052312            -0.052630
# 2942                  -0.751336             0.120432

#exemplos de interpretação dos valores escalonados
#investimento_saude_scaled = 1.37	- País investe bem acima da média global em saúde
#investimento_saude_scaled = -1.01	- País com baixo investimento em saúde
#escolaridade_scaled = -0.26	    - Escolaridade um pouco abaixo da média
#escolaridade_scaled = 0.12	        - Escolaridade ligeiramente acima da média

#Em resumo: Essas variáveis ajudam o modelo a prever a expectativa de vida ao relacionar fatores econômicos e educacionais que influenciam diretamente as condições de saúde e qualidade de vida da população
