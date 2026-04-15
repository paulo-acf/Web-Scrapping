import requests # Baixa arquivos e páginas da internet
import os # Módulo do Python que permite interagir com um sistema operacional (no meu caso, Windows)
import bs4 # Analisa o HTML da página (bs4 = Beautiful Soup 4)
from urllib.parse import urljoin
# Parse --> Analisar e quebrar algo em partes menores (ler um texto e entender a estrutura dele)
# Para simplificar e economizar, a web usa muitos caminhos relativos ("links incompletos")
# A função urljoin do "submódulo" urllib.parse permite juntar •uma URL base a •um caminho relativo.
# Exemplo:
#    •./ --> Diretório atual
#    •../ --> Volte um nível acima
#    •../../ --> Volte dois níveis acima
#    •"http://books.toscrape.com/catalogue/page-1.html" + "../page-2.html"
#    • = "http://books.toscrape.com/catalogue/page-2.html")

http = "https://books.toscrape.com/" # Escolhi este site porque ele é próprio para treino de Web Scraping

os.makedirs("Ecletismo literário", exist_ok=True)
# Função makedirs do módulo os --> Permite criar pastas (diretórios)
# Uma pasta chamada "Ecletismo literário" será criada
# exist_ok=True --> Se a pasta "Ecletismo literário" já existir, não haverá qualquer problema

while True: # Repita algo para sempre até algo mandar parar (break)
    print(f"Baixando: {http}")

    resposta = requests.get(http) # Requisita a página da variável http
    resposta.raise_for_status() # Se o status for 200, o programa segue normalmente

    soup = bs4.BeautifulSoup(resposta.text, "html.parser")
    # resposta.text:
    #    •Resultado --> <html><body><div><img src="x.jpg"></div></body></html>
    #    •É como se fosse uma sopa de letrinhas, todas bem misturadas
    # bs4.BeautifulSoup --> É o que organiza as letreinhas da sopa para o Python ler
    # html.parser --> Lê a HTML da variável resposta
    # html.parser --> Lê o HTML da resposta e o transforma em uma estrutura organizada (árvore)








