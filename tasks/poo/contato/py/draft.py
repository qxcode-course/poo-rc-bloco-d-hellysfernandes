class Contact:
    def __init__(self):
        self.__favorited: bool = False
        self.__fones: list[Fone] = []
        self.__name: str = ""

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f"- {self.__name} []"

class Fone:
    def __init__(self):
        self.__id: str = ""
        self.__nunber: str = ""

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__nunber
    
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
        else:
            print("Fail: comando nao encontrado")
main()