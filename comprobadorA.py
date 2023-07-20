from bs4 import BeautifulSoup
import requests

def productos_mercadoLibre():
    # Obtener el contenido HTML de la página web
    url = 'https://ofertas.mercadolibre.com.ve/ofertas-de-las-semanas#nav-header'
    response = requests.get(url)
    html = response.content
    # Crear un objeto BeautifulSoup con el contenido HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Buscar todos los elementos div que cumplan las condiciones
    titulos = soup.find_all('h2', {'class': 'ui-search-item__title shops__item-title'})
    precios = soup.find_all('span', {'class': 'andes-money-amount ui-search-price__part shops__price-part andes-money-amount--cents-superscript'})
    # Lista para almacenar los resultados
    resultados = []
    # Iterar sobre los títulos y precios y agregarlos a la lista de tuplas
    for titulo, precio in zip(titulos, precios):
        resultados.append([titulo.text, precio.text])
    # Retornar la lista completa
    return resultados

productos = productos_mercadoLibre()
for producto in productos:
    lista=(', '.join(producto))
    print(lista)

