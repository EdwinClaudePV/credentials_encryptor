from cryptography.fernet import Fernet
import json

class Credential:
    """A simple example class"""
    def __init__(self, data):
        self.username = data['username']
        self.password = data['password']

    def __str__(self):
        return self.username + " --> " + self.password

class Programm:

    def __init__(self):
        self.key = self.read_key()
        self.filename = self.get_filename()
        self.credentials = None
        self.decrypt()

    def read_key(self):
        print("Enter the key : ")
        key = input()
        try:
            f = open(key, "rb")
            key = f.read()
        except IOError:
            key = self.write_key()
        return key
        
    def write_key(self):
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

    def read_data(self):
        with open(self.filename, "rb") as file:
            # read all file data
            file_data = file.read()
        return file_data

    def write_data(self, data):
        with open(self.filename, "wb") as file:
            file.write(data)


    def get_filename(self):
        print("Enter the filename : ")
        filename = input()
        return filename

    def encrypt(self):
        '''

        '''
        f = Fernet(self.key)
        file_data = self.read_data()
        encrypted_data = f.encrypt(file_data)
        self.write_data(encrypted_data)

    def decrypt(self):
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        f = Fernet(self.key)
        file_data = self.read_data()
        decrypted_data = f.decrypt(file_data)
        self.write_data(decrypted_data)

    def list_credentials(self):
        if self.credentials is None:
            self.parse_data()

        for key in self.credentials.keys():
            print(key)


    def search_credential(self):
        if self.credentials is None:
            self.parse_data()

        print('Entrer the credential to search :')
        search = input()
        print(self.credentials[search])

    def parse_data(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)

        self.credentials = {}

        for d in data['credentials']:
            self.credentials[d['name']] = Credential(d)

    def quit(self):
        self.credentials.clear()
        self.encrypt()
        print('End programm !!!')   

if __name__ == "__main__":
    prog = Programm()
        
    switcher = {
        1: prog.list_credentials,
        2: prog.search_credential,
        3: prog.quit
        }

    action = 0

    while action != 3:
        print("1 : List the credentials")
        print("2 : Search a credentials")
        print("3 : Quit")
        print("Enter what do you do ? : ")

        try:
            action = int(input())
            func = switcher.get(action, "nothing")
            func()
        except ValueError:
            print('Error in action\'s format')
        