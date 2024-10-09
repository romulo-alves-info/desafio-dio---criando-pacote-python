from setuptools import setup, find_packages

setup(
    name='zoonoses_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'seaborn',
        'matplotlib',
        'scikit-learn'
    ],
    package_data={
        'zoonoses_analysis': ['data/*.csv'],  # Incluir arquivos CSV do diretório data/
    },
    include_package_data=True,  # Para incluir arquivos de dados
)
