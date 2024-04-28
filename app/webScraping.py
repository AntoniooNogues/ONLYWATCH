import requests
from bs4 import BeautifulSoup
import time

# URL de la página de películas en JustWatch
base_url = 'https://www.justwatch.com'
url = base_url + '/es/peliculas'

# Lista para almacenar los datos de las películas
movies = []

while url:
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar las secciones de películas
        movies_section = soup.find_all('div', class_='title-list-grid__item')

        # Extraer datos de cada película
        for section in movies_section:
            time.sleep(1)
            # Obtener el título de la película
            titulo = section.find('img', "picture-comp__img")['alt']
            link = section.find('a', class_="title-list-grid__item--link")['href']
            img_tag = section.find('img', "picture-comp__img")
            if img_tag:
                img = img_tag['data-src'] if 'data-src' in img_tag.attrs else img_tag['src']
            else:
                img = None

            # Agregar detalles a la lista de películas
            link_response = requests.get(base_url + link)
            if link_response.status_code == 200:
                link_soup = BeautifulSoup(link_response.text, 'html.parser')
                article_block = link_soup.find('article', class_='article-block')
                if article_block is not None:
                    sinopsis = article_block.find('div').text
                else:
                    sinopsis = "No esta disponible"
                anyo_estreno = link_soup.find('span', class_='text-muted').text
                director = link_soup.find('span', class_='title-credit-name').text

                movies.append({
                    'title': titulo,
                    'link': link,
                    'imagen': img,
                    'sinopsis': sinopsis,
                    'anyo_estreno': anyo_estreno,
                    'director': director
                })

        # Buscar el enlace a la siguiente página
        next_page = soup.find('a', {'rel': 'next'})
        url = base_url + next_page['href'] if next_page else None

    else:
        print("Error al obtener datos de la página.")
        break

# Mostrar las películas obtenidas
for movie in movies:
    print(f"Título: {movie['title']}")
    print(f"Enlace: https://www.justwatch.com{movie['link']}")
    print(f"Imagen: {movie['imagen']}")
    print(f"Sinopsis: {movie['sinopsis']}")
    print(f"Año de estreno: {movie['anyo_estreno']}")
    print(f"Director: {movie['director']} \n")