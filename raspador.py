import requests # Baixa arquivos e páginas da internet
import os # Módulo do Python que permite interagir com um sistema operacional (no meu caso, Windows)
import bs4 # Analisa o HTML da página (bs4 = Beautiful Soup 4)
import time # Módulo do Python que permite usar funções relacionadas a tempo
from urllib.parse import urljoin
# Parse --> Analisar e quebrar algo em partes menores (em outras palavras, ler um texto e entender a estrutura dele)
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
    resposta.raise_for_status() # Se o status for 2xx (200–299), o programa segue normalmente

    soup = bs4.BeautifulSoup(resposta.text, "html.parser")
    # resposta.text:
    #    •Resultado --> <html><body><div><img src="x.jpg"></div></body></html>
    #    •Acima, é como se fosse uma "sopa de letrinhas", todas bem misturadas
    # bs4.BeautifulSoup --> É o que organiza essas letrinhas da sopa (HTML) para que o Python possa ler
    # html.parser --> Interpreta o HTML bruto para que o BeautifulSoup possa montar a estrutura
    # Parece óbvio, mas é só para ficar claro:
    #    •Aqui, o "bs4" é necessário porque houve "import bs4"
    #    •Se houvesse "from bs4 import BeautifulSoup", a classe (BeautifulSoup) já estaria disponível de forma direta (sem o "bs4")

    imagensss = soup.select("article.product_pod img")
    # "article.product_pod img" vem do html do site (vide abaixo):
    #     <article class="product_pod">
    #         <img src="imagem.jpg">
    #     </article>
    # Em outras palavras --> Ache a imagem que está dentro do produto

    for imagem in imagensss:
        img_http = urljoin(http, imagem["src"]) # De cada img em imagens, quero apenas o src (que é onde está a imagem)

        print(f"Baixando a imagem: {img_http}")

        try:
            img_resposta = requests.get(img_http, timeout = 10) # timeout --> Quanto tempo o programa deve esperar antes de desistir     
            img_resposta.raise_for_status() # Se o status for 2xx (200–299), o programa segue normalmente
        except requests.exceptions.RequestException: # Engloba praticamente todos os erros relacionados a requisições
            print("Erro ao baixar imagem. Tentando baixar a próxima...")
            continue # Continue e volte novamente para o for acima

        caminho_do_arquivo = os.path.join( # os.path.join --> Junta •o nome da pasta com •o nome do arquivo (imagem baixada)
            "Ecletismo literário",
            os.path.basename(img_http) # Pega o nome do arquivo (imagem baixada)
            # Exemplo --> "Ecletismo literário/imagem.jpg"
        )

        with open(caminho_do_arquivo, "wb") as arquivo_aberto:
        # with open (...) as:
        #    •Abre um arquivo localizado no caminho_do_arquivo
        #    •Garante que o arquivo aberto será fechado depois ao final do bloco
        # wb --> •"w" (escrita) •"b" (binária)
            arquivo_aberto.write(img_resposta.content) # Escreve o conteúdo da resposta de img_resposta no arquivo aberto
        time.sleep(0.5) # Intervalo em x segundos entre cada download (para evitar travamentos)

    botao_next = soup.select_one("li.next a")
    # soup --> HTML já organizado pelo BeautifulSoup
    # select_one --> Retorna o primeiro elemento do HTML que corresponde ao seletor entre ()
    # "li.next a" é a forma "abreviada" (seletor CSS) de:
    #    <li class="next">
    #        <a href="page-2.html">next</a>
    #    </li>
    # Significado --> Encontre o próximo botão "next"

    if not botao_next:
        break

    http = urljoin(http, botao_next["href"])
    # href --> hyperlink reference (é o que leva para a próxima página)