import docx2txt


def convert_doc_to_txt():
    employees_file = docx2txt.process("Employees.docx")
    with open("Employees.txt", "w") as text_file:
        print(employees_file, file=text_file)
    return True


if __name__ == "__main__":
    pass
