# (1) - Crregamento das bibliotecas

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

os.system('cls')

# (2) - Entrada de dados
arquivo = "dados_brutos.csv" # Arquivo de dados
dados_df = pd.read_csv(arquivo, header=0, delimiter=";")
dados = dados_df.to_dict('list') # Converte para um DICT de listas

# (3) - Processamento dos dados
# Criação das listas de valores intermediários para análise posterior
area = []
volume = []
densidade = []
tensao = []

# Preencher as listas acima com dados
tamanho = len(dados["ID"]) # Pega o número de dados da coluna ID
contador = range(tamanho) # Cria o contador do laço com o tamanho certo

for i in contador: # Cria um laço sobre todos os dados
    raio = dados["Diâmetro (mm)"][i] / 2.0 # Cálculo do raio
    A = np.pi * (raio ** 2)   # Cálculo da área
    area.append(A)
    
    h = dados["Altura (mm)"][i] # Pega a altura da peça
    vol = A * h     # Cálculo da altura
    
    volume.append(vol)  # Adiciona o volume aos dados
    
    m = dados["Massa (g)"][i] # Pega a massa da peça
    den = m/vol     # Cálculo da densidade
    densidade.append(den)   #Adiciona a densidade dos dados
    
    res = dados["Resistência (kgf)"][i] #Pega a resistência da peça
    T = res/A   # Cálculo da tensão
    
    tensao.append(T)    #Adiciona a tensão aos dados
    
    
    # Identificação dos outliers a partir da informação dos boxplots
    # vetore ----
outliers_densidade = []
outliers_tensao = []
    
for i in contador:
    den = densidade[i] # Pega o valor da densidade da peça
    if (den < 0.000983):
        ID_ruim = dados["ID"][i]
        outliers_densidade.append(ID_ruim)
    T = tensao[i]
    if (T < 2.01):
        ID_ruim = dados["ID"][i]
        outliers_tensao.append(ID_ruim)
#Estudo de comparaçãoPearson
matriz = [dados["Resistência (kgf)"],
          densidade,
          dados["Altura (mm)"],
          dados["Diâmetro (mm)"],
          dados["Massa (g)"],
          area]
coef_pearson = np.corrcoef(matriz) # Realiza a correlação

print(coef_pearson)

rotulos = ["Resist.", "Densidade", "Altura", "Diâmetro" "Massa", "Área"]
sns.heatmap(coef_pearson, annot=True, xticklabels=rotulos)
plt.show()


# (4) - Apresentação dos resultados
# print("Dados brutos originais")
# print(dados)
# print(tensao)
# print(densidade)
# print(len(densidade))
# print(contador)


# # Criação de alguns boxplots para tentar achar os outliers
# plt.boxplot(dados["Massa (g)"])
# plt.title("Boxplot da massa")
# plt.show()

# plt.boxplot(dados["Resistência (kgf)"])
# plt.title("Boxplot da massa")
# plt.show()

# plt.boxplot(densidade)
# plt.title("Boxplot da massa")
# plt.show()

# plt.boxplot(tensao)
# plt.title("Boxplot da massa")
# plt.show()

# print("Outliers de densidade: ", outliers_densidade)
# print("Outliers de tensão", outliers_tensao)

# Desenho da dispersão dos dados para avaliar a resistência
#plt.scatter(densidade, dados["Resistência (kgf)"])
plt.title("R")
plt.scatter(densidade, dados["Resistência (kgf)"])
plt.scatter(densidade, dados["Resistência (kgf)"])