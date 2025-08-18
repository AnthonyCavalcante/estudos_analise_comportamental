from setuptools import setup, find_packages

# Lendo a lista de dependências do requirements.txt
# Isso evita duplicar a informação em dois lugares.
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='analise-semanal=4',  # Nome do seu projeto (sem espaços ou caracteres especiais)
    version='0.1.0',  # Versão inicial do seu projeto
    
    author='Anthony Cavalcante',  # Seu nome ou o nome da sua equipe
    author_email='anthonycavalcante@gmail.com',  # Seu e-mail de contato
    
    description='desafio semanal do Gemini',  # Uma frase curta sobre o projeto
    
    # Encontra automaticamente todos os pacotes (pastas com __init__.py) no seu projeto
    packages=find_packages(),
    
    # Define as dependências que serão instaladas junto com o seu pacote
    install_requires=requirements,
    
    # Classificadores para ajudar a categorizar seu projeto (opcional, mas boa prática)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # Versão mínima do Python necessária para rodar seu projeto
)