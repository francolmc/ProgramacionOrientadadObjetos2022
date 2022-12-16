import requests

try:
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    print(f'Codigo: {response.status_code}')
    print(f'Contenido: {response.content.decode()}')
    print(f'JSON: {response.json()}')
    data = response.json()
    results = data['results']
    for character in results:
        print(f'Nombre: {character["name"]}')
except requests.HTTPError as http_error:
    print(http_error)
except Exception as ex:
    print(ex)