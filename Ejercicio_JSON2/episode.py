class Episode:
    def __init__(self) -> None:
        self.__name = ''
        self.__air_date = ''
        self.__episode = ''

    def setName(self, value: str):
        self.__name = value

    def getName(self) -> str:
        return self.__name

    def setAirDate(self, value: str):
        self.__air_date = value

    def getAirDate(self) -> str:
        return self.__air_date

    def setEpisode(self, value: str):
        self.__episode = value

    def getEpisode(self):
        return self.__episode
