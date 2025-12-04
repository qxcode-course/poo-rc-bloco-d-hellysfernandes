class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number
    
    def setId(self, id: str) -> str:
        self.__id = id

    def setNumber(self, number: str) -> str:
        self.__number = number
    
    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"

class Contact: 
    def __init__(self, name: str):
        self.__favorited: bool = False
        self.__fone: list[Fone] = []
        self.__name = name

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        self.__fone.append(fone)

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fone):
            self.__fone.pop(index)
        else:
            raise Exception("fail: index errado")
        
    def toggleFavorited(self) -> None:
        self.__favorited = not self.__favorited

    def isFavorited(self) -> None:
        return self.__favorited

    def getFones(self) -> str:
        return self.__fone
    
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> str:
        self.__name = name

    def __str__(self) -> str:
        lista = ", ".join(str(f) for f in self.__fone)
        prefix = "@" if self.__favorited else "-"
        return f"{prefix} {self.__name} [{lista}]"

class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def findPos(self, name: str) -> int:
        for i, c in enumerate(self.__contacts):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]) -> None:
        pos = self.findPos(name)

        if pos != -1:
            for f in fones:
                self.__contacts[pos].addFone(f.getId(), f.getNumber())
        else:
            contato = Contact(name)
            for f in fones:
                contato.addFone(f.getId(), f.getNumber())
            self.__contacts.append(contato)
            self.__contacts.sort(key=lambda x: x.getName().lower())
    
    def getContact(self, name: str) -> Contact:
        pos = self.findPos(name)
        if pos == -1:
            raise Exception("fail: nao encontrado")
        return self.__contacts[pos]
    
    def rmContact(self, name: str) -> None:
        pos = self.findPos(name)
        if pos == -1:
            raise Exception("fail: nao encontrado")
        self.__contacts.pop(pos)

    def search(self, pattern: str) -> list[Contact]:
        result = []
        for c in self.__contacts:
            if pattern.lower() in c.getName().lower():
                result.append(c)
                continue

            for f in c.getFones():
               if (pattern.lower() in f.getId().lower()) or (pattern in f.getNumber()):
                    result.append(c)
                    break
               
        return result
    
    def getFavorited(self) -> list[Contact]:
        return [c for c in self.__contacts if c.isFavorited()]

    def __str__(self) -> str:
        return "\n".join(str(c) for c in self.__contacts)

def  main():

    agenda = Agenda()

    while(True):
        try:
            line: str = input()
            print("$" + line)
            args: list[str] = line.split(" ")

            if args[0] == "end":
                break
            elif args[0] == "show":
                print(agenda)
            elif args[0] == "add":
                name: str = args[1]
                fones = []
                for itens in args[2:]:
                    id, number = itens.split(":")
                    fones.append(Fone(id, number))
                agenda.addContact(name, fones)
            elif args[0] == "rmFone":
                name: str = args[1]
                index: int = int(args[2])
                contato = agenda.getContact(name)
                contato.rmFone(index)
            elif args[0] == "rm":
                name: str = args[1]
                agenda.rmContact(name)
            elif args[0] == "search":
                pattern: str = args[1]
                for c in agenda.search(pattern):
                    print(c)
            elif args[0] == "tfav":
                name: str = args[1]
                contato = agenda.getContact(name)
                contato.toggleFavorited()
            elif args[0] == "favs":
                for c in agenda.getFavorited():
                    print(c)
            else:
                print("fail: comando nao encontrado")

        except Exception as e:
            print(e)

main()