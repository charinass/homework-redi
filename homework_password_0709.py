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
    "Numbers should not be next to each other. Please enter a stronger password." + \
    fg.rs  # I got lazy
MSG_SUCCESS = fg.green+"You saved a new password."+fg.rs


def main():
    while True:
        try:
            print(
                f"Enter a password minimum of {MINCHAR} characters \n- with at least {MINLETTER} upper-case letter \n- at least {MINDIGS} digits \n- two consecutive digits is not allowed.")
            # userPass = stdiomask.getpass("Input password:") # for hidden password
            userPass = input("Input password:")
            if (checkStringValidity(userPass) == True):
                print(MSG_SUCCESS)
                break
            else:
                raise InputError
        except InputError:
            print(MSG_ERROR)


# I should separate each of these in methods because this currently is not a good proctice!!!
def checkStringValidity(userPass):  # this should be #check_string_validity():
    if ((isinstance(userPass, str) == True) and (len(userPass) >= MINCHAR) and (userPass.count(' ') == 0) and (len(re.findall(r'[A-Z]', userPass)) >= MINLETTER) and (len(re.findall(r'[0-9]', userPass)) >= MINDIGS)) and (re.search(DIGIT_PATTERN, userPass) == None):
        return True


class InputError(Exception):
    pass


if __name__ == "__main__":
    main()
