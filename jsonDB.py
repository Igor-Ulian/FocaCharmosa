import json


def addUser(nome):
    with open('dados.json') as json_file:
        data = json.load(json_file)
        data["Usuarios"].append(nome)
        #print(data["Usuarios"])
        json_file.close()

    with open('dados.json', 'w') as outfile:
        json.dump(data, outfile) 


def verifyUser(nome):
    with open('dados.json') as json_file:
        data = json.load(json_file)
        if nome in data["Usuarios"]:
            return True
        else:
            return False

def getFollowersJson():
    with open('dados.json') as json_file:
        data = json.load(json_file)
        return data["Usuarios"]
    


