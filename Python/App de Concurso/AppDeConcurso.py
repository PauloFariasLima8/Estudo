import requests
from bs4 import BeautifulSoup

def buscar_concursos():
    url = 'https://www.pciconcursos.com.br/concursos-abertos/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        concursos = soup.find_all('div', class_='concurso')

        for concurso in concursos:
            titulo = concurso.find('h3').text.strip()
            data = concurso.find('span', class_='data').text.strip()
            print(f'Título: {titulo}\nData: {data}\n')
    else:
        print('Erro ao acessar o site.')

if __name__ == '__main__':
    buscar_concursos()