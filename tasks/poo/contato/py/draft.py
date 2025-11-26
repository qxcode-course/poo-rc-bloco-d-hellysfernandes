class Contact:
    def __init__(self):
        self.__favorited: bool = False
        self.__fones: list[Fone] = []
        self.__name: str = ""

    def addFone(self, telefone: Fone) -> None:
        self.__fones.append()

    def getFone(self):
        return self.__fones
    
    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        fones = ": ".join([str(x) if x else "-----" for x in self.__fones])
        return f"- {self.__name} [{fones}]"

class Fone:
    def __init__(self):
        self.__id: str = ""
        self.__number: str = ""

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number
    
    def Fone(self, id: str, number: str) -> None:
        self.__id = id
        self.__number = number

    def __str__(self) -> str:
        return f"{self.__id}: {self.__number}"

def main():

    contato = Contact()
    telefone = Fone()

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
            telefone.Fone(id,number)
            contato.addFone(id,number)
        else:
            print("Fail: comando nao encontrado")
main()