from bs4 import BeautifulSoup
import requests
import time

# simular um navegador real para evitar bloqueio
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

url = 'https://www.marantextecidos.com.br/'
 
time.sleep(2)

response = requests.get(url, headers=headers)

print(f'Status code: {response.status_code}')


time.sleep(1)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    produtos = soup.find_all(class_="product-link")

    for i, produto in enumerate(produtos, 1):
        print(f'{i} - {produto.text.strip()}')
    
    precos = soup.find_all(class_='product-big-price')

    for i, preco in enumerate(precos, 1):
        print(f'{i} - {preco.text.strip()}')

else:
    print('Erro ao acessar a página', response.status_code)

# pip install beautifulsoup4

# pip install requests