import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(data, column):
    """Plota a distribuição de uma coluna específica."""
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribuição de {column}')
    plt.show()
