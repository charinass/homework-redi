def write_new_file(str_input, file_name):  # inputs str to be written into a file
    with open(file_name, 'w+') as file:
        file.write(str_input)
    return file_name


# outputs the counted str into a file
def write_output_file(read_file, file_name):
    file_name = file_name.replace('.txt', '_output.txt')
    with open(file_name, 'w') as file:
        print(read_file, file=file)


def sorter(some_dict: dict):
    some_dict = dict(
        sorted(some_dict.items(), key=lambda x: x[1], reverse=True))
    return some_dict


def read_a_file(file_name):  # counts number of a character in an entire txt file
    try:
        with open(file_name, 'r') as file:
            read_file = file.read()
            char_count = {}
            for i in read_file.lower():
                if(i.isalnum() == True):
                    char_count[i] = char_count.get(i, 0) + 1
        char_count = dict(sorted(char_count.items()))
        char_count = sorter(char_count)
        return char_count
    except FileNotFoundError:
        return False


# counts number of a character per user-defined number of lines in a file
def read_by_line(num_of_lines: int, file_name):
    try:
        with open(file_name, 'r') as file:
            read_file = file.readlines(num_of_lines)
            per_line = []
            return_list = []
            for i in read_file:
                per_line = i.lower()
                for x in per_line:
                    if(x.isalnum() == True):
                        if [x, per_line.count(x)] not in return_list:
                            return_list.append([x, per_line.count(x)])
        return_list = dict(return_list)
        return_list = sorter(return_list)
        return return_list
    except FileNotFoundError:
        return False


def switcher(choice: int):
    if(choice == 1):  # input and read and write io
        str_input = input("Enter your sentence: ")
        file_name = input("Enter a txt file name: ")
        if(str_input != "" and file_name != ""):
            if(file_name.endswith('.txt') == False):
                file_name = file_name + ".txt"
            file_name = write_new_file(str_input, file_name)
            read_file = read_a_file(file_name)
            write_output_file(read_file, file_name)
        else:
            print("You entered nothing.")
            exit
    elif(choice == 2):  # read only and output
        file_name = input("Enter a txt file name: ")
        if(file_name.endswith('.txt') == False):
            file_name = file_name + ".txt"
        read_file = read_a_file(file_name)
        if (read_file != False):
            write_output_file(read_file, file_name)
        else:
            print("File not found")
    else:
        num_of_lines = int(input(
            "Enter number of lines in the file you want to read: "))
        file_name = input("Enter the file name: ")
        if(file_name.endswith('.txt') == False):
            file_name = file_name + ".txt"
        return_list = read_by_line(num_of_lines, file_name)
        if(return_list != False):
            write_output_file(return_list, file_name)
        else:
            print("File not found")


def main():
    try:
        print("Options:\n[1] Create a new txt file (if file does not exist) \n[2] Output counted characters to a txt file \n[3] Read per line of a txt file")
        choice = int(input("Input Task: "))
        if (choice > 0 and choice < 4):
            switcher(choice)
        else:
            raise ValueError
    except ValueError:
        print("invalid number")
        main()


if __name__ == "__main__":
    main()
