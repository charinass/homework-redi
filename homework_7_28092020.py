from cryptography.fernet import Fernet


def encryptor(func):
    def newmessage(message):
        message = func(message)
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        return encrypted
    return newmessage


def boldfunc(func):
    def newbold(message):
        print(f"\033[1m{func(message)}\033[0m")
    return newbold


def italicfunc(func):
    def newitalic(message):
        print(f"\x1B[3m{func(message)}\x1B[23m")
    return newitalic


def underlinefunc(func):
    def newunderline(message):
        print(f"\033[4m{func(message)}\033[0m")
    return newunderline


@encryptor
def thismessage(message):
    return message


def read_namelist():
    nameslist = []
    with open("names_list.txt", "r", encoding="utf-8") as name:
        nameslist += (i.strip("\n") for i in name.readlines())
    return nameslist


@boldfunc
def lowercase(nameslist):
    """ 
    1. Given a list of names. Find the total number of names starting with lowercase. Use lambda function. 
    """
    lowercasenames = list(filter(lambda x: x == x.lower(), nameslist))
    return lowercasenames


@underlinefunc
def sortednameslist(nameslist):
    """
    2. Sort the words in the list based on their second letter from a to z. Use sorted() and lambda function.
    """
    sortednames = sorted(nameslist, key=lambda x: x[1])
    return sortednames


@italicfunc
def sortlastcharacter(nameslist):
    """
    3. Sort the tuples in the list based on the last character of the second items. Use sorted() and lambda function.
    """
    sortedlastcharacters = sorted(nameslist, key=lambda x: x[-1])
    return sortedlastcharacters


if __name__ == "__main__":

    """
    1. Create three decorator functions namely ⟶ (bold, italic and underline) to decorate a text. Use decorator syntax to use the decorator functions. [HINT: You can use multiple decorators on a function]
    """

    """
    2. Write a decorator function that encrypts a given string message. Use following code to encrypt a string message.
    """
    encrypted = thismessage("Life is beautiful".encode())
    print(encrypted)

    nameslist = read_namelist()
    print(nameslist)
    lowercase(nameslist)
    sortednameslist(nameslist)
    sortlastcharacter(nameslist)
