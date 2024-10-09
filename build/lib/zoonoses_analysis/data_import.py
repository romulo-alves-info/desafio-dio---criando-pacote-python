import pandas as pd

def load_data(file_path):
    """Carrega dados de um arquivo CSV."""
    data = pd.read_csv(file_path)
    return data
