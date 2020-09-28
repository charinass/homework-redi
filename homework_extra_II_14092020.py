a_list = [1, 3, 5, 7, 9, 15, 20]


def find_number(a_number: int):
    res_index = 0
    for i in a_list:
        if(a_number == i):
            return True, a_list.index(a_number)
        else:
            res_index = 0
    if(res_index == 0):
        return False, 0


def find_number_two(a_number, i):
    tmp_list = a_list
    if (tmp_list[i] == a_number):
        return True, tmp_list.index(tmp_list[i])
    else:
        if not(i == (len(tmp_list)-1)):
            i += 1
        else:
            return False, 0
        return find_number_two(a_number, i)


if __name__ == "__main__":
    try:
        # loop
        a_number = int(input("Input number:"))
        res_bool, res_index = find_number(a_number)
        if(res_bool == True):
            print(
                f"Number = {a_number} -> result: Yes, belongs. Index = {res_index}")
        else:
            print(f"Number = {a_number} -> result: No doesn’t belong.")

        # recursive
        res_bool, res_index = find_number_two(a_number, 0)
        if(res_bool == True):
            print(
                f"Number = {a_number} -> result: Yes, belongs. Index = {res_index}")
        else:
            print(f"Number = {a_number} -> result: No doesn’t belong.")

    except ValueError:
        print("not a number")
