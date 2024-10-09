# Zoonoses Analysis

Um pacote Python para análise de dados relacionados a zoonoses. O pacote fornece funcionalidades para importação de dados, análise exploratória, modelagem preditiva e geração de relatórios.

## Instalação

Para instalar o pacote, você pode usar `pip`:

```bash
pip install .
```

Certifique-se de que você tenha as dependências necessárias instaladas:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## Estrutura do Pacote

```
zoonoses_analysis/
│
├── zoonoses_analysis/
│   ├── __init__.py
│   ├── data_import.py
│   ├── exploratory_analysis.py
│   ├── modeling.py
│   └── reporting.py
│
├── tests/
│   ├── __init__.py
│   └── test_zoonoses_analysis.py
│
├── examples/
│   └── example_usage.py
│
├── data/
│   └── dados_zoonoses.csv
│
├── setup.py
└── README.md
```

## Funcionalidades

- **Importação de Dados**: Carrega dados de arquivos CSV.
- **Análise Exploratória**: Realiza análises estatísticas e gera gráficos.
- **Modelagem**: Treina modelos preditivos para zoonoses.
- **Relatórios**: Gera relatórios com métricas de desempenho do modelo.

## Exemplo de Uso

```python
import pandas as pd
from zoonoses_analysis.data_import import load_data
from zoonoses_analysis.exploratory_analysis import plot_distribution
from zoonoses_analysis.modeling import train_model
from zoonoses_analysis.reporting import generate_report

# Carregar os dados
data = load_data('data/dados_zoonoses.csv')

# Análise Exploratória
print(data.describe())
plot_distribution(data, 'idade')

# Modelagem
features = ['idade']
target = 'zoonose'
model = train_model(data, features, target)

# Gerar Relatório
X = data[features]
y = data[target]
generate_report(model, X_test, y_test)
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma `issue` ou enviar um `pull request`.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```