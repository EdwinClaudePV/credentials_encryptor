from cryptography.fernet import Fernet
import base64


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(filename, "wb") as file:
            file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    print("Enter the key : ")
    key = input()
    try:
        f = open(key, "rb")
        key = f.read()
    except IOError:
        write_key()
    finally:
        print("Enter the filename : ")
        filename = input()

        print("Enter what do you do (encrypt(e) or decrypt(d)) : ")
        function = input()

        if function == 'e':
            encrypt(filename, key)
        elif function == 'd':
            decrypt(filename, key)

        f.close()
        
    