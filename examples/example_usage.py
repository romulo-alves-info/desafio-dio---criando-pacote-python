# example_usage.py

import pandas as pd
from zoonoses_analysis.data_import import load_data
from zoonoses_analysis.exploratory_analysis import plot_distribution
from zoonoses_analysis.modeling import train_model
from zoonoses_analysis.reporting import generate_report

# 1. Carregar os dados
#file_path = 'caminho/para/seus_dados.csv'  # Substitua pelo caminho do seu arquivo CSV
file_path = 'data/dados_zoonoses.csv'  # Caminho para o arquivo CSV
data = load_data(file_path)

# 2. Análise Exploratória
print("Análise Exploratória:")
print(data.describe())  # Exibe estatísticas descritivas

# Plotar a distribuição da idade
plot_distribution(data, 'idade')

# 3. Modelagem
features = ['idade']  # Substitua por outras características se necessário
target = 'zoonose'
model = train_model(data, features, target)

# 4. Geração de Relatório
# Para gerar o relatório, precisamos dividir os dados em conjunto de treino e teste novamente
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gerar o relatório
generate_report(model, X_test, y_test)
