import requests

try:
    response = requests.get('https://pokeapi.co/api/v2/ability')

    print(response)
    print(f'codigo de respuesta: {response.status_code}')
    print(f'contenido de la respuest en bytes decodificado: {response.content.decode()}')
    data = response.json()
    print(f'contenido de la respuest en JSON: {data}')
    print(f'la cantidad de registros es: {data["count"]}')
except requests.HTTPError as http_err:
    print(http_err)
except Exception as err:
    print(err)
