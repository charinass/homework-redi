input_file = 'input.txt'
output_file = 'output.txt'
KEY = 3


def encrypt_file():
    with open(input_file, 'r') as file:
        data = file.read()
        encrypted_data = ""
        for i in data:
            encrypted_data += chr(ord(i) ^ KEY)
    encrypted_data = encrypted_data.encode()
    with open(output_file, 'w+b') as en_file:
        en_file.write(encrypted_data)


def unencrypt_file():
    with open(output_file, 'r+b') as file:
        data = file.read()
        unencrypted_data = ""
        temp = ""
        for i in data:
            temp = chr(i ^ KEY)
            unencrypted_data += chr(i ^ KEY)
    print(unencrypted_data)


if __name__ == "__main__":
    encrypt_file()
    unencrypt_file()
