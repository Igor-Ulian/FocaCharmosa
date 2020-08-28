import json
import os

path = os.getcwd().replace("src", "")

data_path = f'{path}data\\dados.json'
queue_path = f'{path}data\\followers_in_queue.json'

def verifyPath():
    if not os.path.isfile(f'{path}data/followers_in_queue.json'):
        file = open(f'{path}data/followers_in_queue.json', "w") 
        file.write("") 
        file.close()
        print("followers_in_queue.json was crated!")

    if not os.path.isfile(f'{path}data/dados.json'):
        file = open(f'{path}data/dados.json', "w") 
        file.write("") 
        file.close() 
        print("dados.json was crated!")

verifyPath()

def addUser(nome): # add user to json file
    with open(data_path) as json_file:
        data = json.load(json_file)
        data["Usuarios"].append(nome)
        json_file.close()

    with open(data_path, 'w') as outfile:
        json.dump(data, outfile) 


def verifyUser(nome): # virify if user 'nome' is on json file
    with open(data_path) as json_file:
        data = json.load(json_file)
        if nome in data["Usuarios"]:
            return True
        else:
            return False

def getFollowersJson(): # return all json file users
    with open(data_path) as json_file:
        data = json.load(json_file)
        return data["Usuarios"]

def deleteFollowerInQueue(user):
    with open(queue_path) as json_file:
        data = json.load(json_file)
        if user in data["Followers"]:
            data["Followers"].remove(user)
            json_file.close()

    with open(queue_path, 'w') as outfile:
        json.dump(data, outfile) 

def addFollowerInQueue(user): 
    if not verifyFollowersInQueue(user):
        with open(queue_path) as json_file:
            data = json.load(json_file)
            data["Followers"].append(user)
            json_file.close()

        with open(queue_path, 'w') as outfile:
            json.dump(data, outfile) 

def verifyFollowersInQueue(user):
    with open(queue_path) as json_file:
        data = json.load(json_file)
        if user in data["Followers"]:
            json_file.close()
            return True
        else:
            json_file.close()
            return False

def getQueueList():
    with open(queue_path) as json_file:
        data = json.load(json_file)
        return data["Followers"]