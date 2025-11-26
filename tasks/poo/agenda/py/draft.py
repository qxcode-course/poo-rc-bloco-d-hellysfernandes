class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

class Contact: 
    def __init__(self):
        self.__favorited: bool = False
        self.__fone: list[Fone] = []
        self.__name: str = ""


class Fone:
    def __init__(self):
        self.__id: str = ""
        self.__number: str = ""

    def getId(self) -> str:
        return self.__id
    
    def getName(self) -> str:
        return self.__number
    
    def __str__(self) -> str:
        return f"{self.__id} {self.__number}"