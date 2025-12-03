class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def isValid(self) -> bool:
        valid = "0123456789()."
        for caract in self.__number:
            if caract not in valid:
                return False
        return True

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number
    
    def setId(self, id: str) -> str:
        self.__id = id

    def setNunber(self, number) -> str:
        self.__number = number
    
    def Fone(self, id: str, number: str) -> None:
        self.__id = id
        self.__number = number

    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, ):
        self.__favorited: bool = False
        self.__fones: list[Fone] = []
        self.__name: str = ""

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: invalid number")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: index errado")

    def toogleFavorited(self):
        self.__favorited = not self.__favorited

    def getFone(self):
        return self.__fones
    
    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        fones = ", ".join([str(x) for x in self.__fones])
        if self.__favorited:
            return f"@ {self.__name} [{fones}]"
        else:
            return f"- {self.__name} [{fones}]"

def main():

    contato = Contact()

    while (True):

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(contato)
        elif args[0] == "init":
            name: str = args[1]
            contato.setName(name)
        elif args[0] == "add":
            id: str = args[1]
            number: str = args[2]
            contato.addFone(id, number)
        elif args[0] == "rm":
            index = int(args[1])
            contato.rmFone(index)
        elif args[0] == "tfav":
            contato.toogleFavorited()
        else:
            print("Fail: comando invalido")
main()