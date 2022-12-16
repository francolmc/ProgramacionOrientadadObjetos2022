class Episode():
    def __init__(self) -> None:
        self.__name = ''
        self.__air_date = ''
        self.__episode = ''

    def getName(self) -> str:
        return self.__name

    def setName(self, value: str):
        self.__name = value

    def getAirDate(self) -> str:
        return self.__air_date

    def setAirDate(self, value: str):
        self.__air_date = value

    def getEpisode(self) -> str:
        return self.__episode

    def setEpisode(self, value: str):
        self.__episode = value
