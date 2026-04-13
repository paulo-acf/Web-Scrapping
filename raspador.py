


import requests # Baixa arquivos e páginas da internet
import os # Módulo do Python que permite interagir com um sistema operacional (no     meu caso, Windows)
import bs4 # Analisa o HTML da página (bs4 = Beautiful Soup 4)

http = '' # AINDA VOU COLOCAR A URL AQUI

os.makedirs('....ismo', exist_ok=True)
# Uma pasta chamada     ....ismo será criada
# exist_ok=True --> Se a pasta      ...ismo já existir, não haverá problema algum

while busca_gifs: # PRECISO VERIFICAR QUAL É O "SINAL DE PARADA" (OU OUTRA FORMA APROPRIADA) PARA INPLEMENTAR DA FORMA CORRETA
    print('Baixando da página %s...' % http) 
    # %s --> Espaço reservado para alguma outra coisa
    # Significado --> "Coloque o valor da variável http no lugar do %s"
    res = requests.get(http)
    res.raise_for_status()

    if busca_gifs == 0:
        break















