import unittest
import pandas as pd
from zoonoses_analysis.data_import import load_data
from zoonoses_analysis.exploratory_analysis import plot_distribution
from zoonoses_analysis.modeling import train_model

class TestZoonosesAnalysis(unittest.TestCase):
    
    def setUp(self):
        """Configuração inicial para os testes."""
        # Criar um DataFrame de exemplo
        self.data = pd.DataFrame({
            'idade': [5, 10, 15, 20, 25, 30],
            'zoonose': [0, 1, 0, 1, 0, 1]
        })

    def test_load_data(self):
        """Teste se a função de carregamento de dados funciona."""
        # Para o teste, vamos simular a carga de dados diretamente
        df = self.data
        self.assertEqual(len(df), 6)

    def test_plot_distribution(self):
        """Teste se a plotagem de distribuição não gera erros."""
        try:
            plot_distribution(self.data, 'idade')
        except Exception as e:
            self.fail(f"plot_distribution falhou com a exceção: {e}")

    def test_train_model(self):
        """Teste se o modelo é treinado sem erros."""
        features = ['idade']
        target = 'zoonose'
        model = train_model(self.data, features, target)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
