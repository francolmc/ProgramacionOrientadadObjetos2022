import requests
from episode import Episode

def searchEpisode(name: str) -> Episode:
    url = 'https://rickandmortyapi.com/api/episode'
    response = requests.get(url)
    results = response.json()
    episode = Episode()
    for item in results['results']:
        if item['name'] == name:
            episode.setName(item['name'])
            episode.setAirDate(item['air_date'])
            episode.setEpisode(item['episode'])
    return episode

searchName = input('Nombre a buscar: ')
result = searchEpisode(searchName)
print(f'name: {result.getName()} date: {result.getAirDate()} episode: {result.getEpisode()}')

