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
        return f"\033[1m{func(message)}\033[0m"
    return newbold


def italicfunc(func):
    def newitalic(message):
        return f"\x1B[3m{func(message)}\x1B[23m"
    return newitalic


def underlinefunc(func):
    def newunderline(message):
        return f"\033[4m{func(message)}\033[0m"
    return newunderline


@encryptor
def thismessage(message):
    return message


@underlinefunc
def formatted_text(message):
    return message


if __name__ == "__main__":

    """
    1. Write a decorator function that encrypts a given string message. Use following code to encrypt a string message.
    """
    encrypted = thismessage("Life is beautiful".encode())
    print(encrypted)

    """
    2. Write a decorator function that encrypts a given string message. Use following code to encrypt a string message.
    """
    message = "Life is beautiful"
    print(formatted_text(message))

    ############################################################################

    """ 
    1. Given a list of names. Find the total number of names starting with lowercase. Use lambda function. 
    """
    nameslist = []
    with open("names_list.txt", "r", encoding="utf-8") as name:
        for i in name.readlines():
            nameslist.append(i.strip("\n"))
    print(f"\033[95mList of names:\033[0m \n{nameslist}")

    lowercasenames = list(filter(lambda x: x == x.lower(), nameslist))
    print(f"\033[95mLowercase names:\033[0m \n{lowercasenames}")

    """
    2. Sort the words in the list based on their second letter from a to z. Use sorted() and lambda function.
    """
    sortednames = sorted(nameslist, key=lambda x: x[1])
    print(f"\033[95mSorted in second letter names:\033[0m \n{sortednames}")

    """
    3. Sort the tuples in the list based on the last character of the second items. Use sorted() and lambda function.
    """
    sortedlastcharacters = sorted(sortednames, key=lambda x: x[-1])
    print(f"\033[95mSorted last characters:\033[0m \n{sortedlastcharacters}")
