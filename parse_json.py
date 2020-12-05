import json

if __name__ == "__main__":
    with open('passwords.json') as json_file:
        data = json.load(json_file)
        for p in data['passwords']:
            print('Name: ' + p['name'])
            print('Username: ' + p['username'])
            print('Password: ' + p['password'])
            print('')