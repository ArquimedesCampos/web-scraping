from bs4 import BeautifulSoup
import requests

def productos_ebay():
    
    # Obtener el contenido HTML de la página web
    url = 'https://www.ebay.com/globaldeals?_trkparms=pageci%3Ad61be457-184b-11ee-9b83-42cd9888637b%7Cparentrq%3A1317696e1890a744b15136c4fffec7ac%7Ciid%3A1'
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup con el contenido HTML
    soup = BeautifulSoup(html, 'html.parser')
    

    # Buscar todos los elementos que contengan la clase 'first'
    precios = soup.find_all('span', {'class': 'first'})
    titulos = soup.find_all('span', {'class': ['ebayui-ellipsis-2', 'ebayui-ellipsis-3'], 'itemprop': 'name'})
    for titulo in titulos:
        contenido = titulo.text

    # Filtrar los precios que sean menores a US $299.00
    precios_filtrados = [precio for precio in precios if float(precio.text.strip().replace('US $', '').replace('\xa0', '')) < 349.00]

    productos = [ (titulo.text, precio.text) for titulo, precio in zip(titulos, precios) ]
    lista_de_productos = '\n'.join([f'{titulo} - {precio}' for titulo, precio in productos])
    return lista_de_productos
productos = productos_ebay()
print(productos)

