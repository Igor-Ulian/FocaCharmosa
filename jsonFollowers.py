import json

def addUser(nome): # add user to json file
    with open('dados.json') as json_file:
        data = json.load(json_file)
        data["Usuarios"].append(nome)
        json_file.close()

    with open('dados.json', 'w') as outfile:
        json.dump(data, outfile) 


def verifyUser(nome): # virify if user 'nome' is on json file
    with open('dados.json') as json_file:
        data = json.load(json_file)
        if nome in data["Usuarios"]:
            return True
        else:
            return False

def getFollowersJson(): # return all json file users
    with open('dados.json') as json_file:
        data = json.load(json_file)
        return data["Usuarios"]

def deleteFollowerInQueue(user):
    with open('followers_in_queue.json') as json_file:
        data = json.load(json_file)
        if user in data["Followers"]:
            data["Followers"].remove(user)
            json_file.close()

    with open('followers_in_queue.json', 'w') as outfile:
        json.dump(data, outfile) 

def addFollowerInQueue(user): 
    if not verifyFollowersInQueue(user):
        with open('followers_in_queue.json') as json_file:
            data = json.load(json_file)
            data["Followers"].append(user)
            json_file.close()

        with open('followers_in_queue.json', 'w') as outfile:
            json.dump(data, outfile) 

def verifyFollowersInQueue(user):
    with open('followers_in_queue.json') as json_file:
        data = json.load(json_file)
        if user in data["Followers"]:
            json_file.close()
            return True
        else:
            json_file.close()
            return False

def getQueueList():
    with open('followers_in_queue.json') as json_file:
        data = json.load(json_file)
        return data["Followers"]