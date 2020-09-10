# this checks for a valid password
import re
import stdiomask
from sty import fg, rs

### edit constants here ###
MINCHAR = 8  # minimum characters for password
MINLETTER = 1  # minimum number of letters
MINDIGS = 2  # minimum number of digits
DIGIT_PATTERN = r'\d\d'  # consecutive digits pattern
MSG_ERROR = fg.red+"Invalid password. Try again."+fg.rs  # error messages
MSG_ERROR_NUM_INV = fg.red + \
    "Numbers should not be next to each other. Please enter a stronger password."+fg.rs
MSG_SUCCESS = fg.green+"You saved a new password."+fg.rs


def main():

    print(
        "Enter a password minimum of {} characters \n- with at least {} upper-case letter \n- at least {} digits \n- two consecutive digits is not allowed.".format(MINCHAR, MINLETTER, MINDIGS))
    # userPass = stdiomask.getpass("Input password:") # for hidden password
    userPass = input("Input password:")
    checkStringValidity(userPass)


def checkStringValidity(userPass):
    if ((isinstance(userPass, str) == True) and (len(userPass) >= MINCHAR) and (userPass.count(' ') == 0) and (len(re.findall(r'[A-Z]', userPass)) >= MINLETTER) and (len(re.findall(r'[0-9]', userPass)) >= MINDIGS)):
        charSearch(userPass)
        print(MSG_SUCCESS)  # save password
    else:
        print(MSG_ERROR)
        main()


def charSearch(userPass):  # checks whether numbers are next to each other
    if (re.search(DIGIT_PATTERN, userPass) != None):
        print(MSG_ERROR_NUM_INV)
        main()


if __name__ == "__main__":
    main()
