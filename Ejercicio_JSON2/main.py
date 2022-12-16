from typing import Any
import requests
from episode import Episode

def getData() -> Any:
    try:
        url = "https://rickandmortyapi.com/api/episode"
        response = requests.get(url)
        result = response.json()
        return result
    except Exception as ex:
        print(ex)

def search(name: str) -> Episode:
    data = getData()
    episode = Episode()
    for item in data["results"]:
        if item["name"] == name:
            episode.setName(item["name"])
            episode.setAirDate(item["air_date"])
            episode.setEpisode(item["episode"])
            return episode
    return episode

def isKey(values: dict, key: str) -> bool:
    if key in values:
        return True
    return False

def search2(name: str) -> Episode:
    episode = Episode()
    try:
        url = f'https://rickandmortyapi.com/api/episode?name={name}'
        response = requests.get(url)
        result = response.json()
        if isKey(result, 'error'):
            return episode
        else:
            episode.setName(result["results"][0]["name"])
            episode.setAirDate(result["results"][0]["air_date"])
            episode.setEpisode(result["results"][0]["episode"])
            return episode
    except:
        return episode

searchName = input('Ingresar nombre del episodio: ')
episode = search2(searchName)
if episode.getName() == '':
    print('Episodio no encontrado.')
else:
    print(f'name: {episode.getName()}, air date: {episode.getAirDate()}, episode: {episode.getEpisode()}')
