import oauth2
import urllib
import json
import time
import tweepy
from random import randint
from jsonDB import addUser
from jsonDB import verifyUser
from jsonDB import getFollowersJson
import credentials

# Replace with your own keys/tokens 
api_key = credentials.api_key
api_secret_key = credentials.api_secret_key
bearer_token = credentials.bearer_token
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

consumer = oauth2.Consumer(api_key,api_secret_key)
token = oauth2.Token(access_token,access_token_secret)
client = oauth2.Client(consumer,token)

auth=tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

def getRequests():
    while True:
        requisicao = client.request('https://api.twitter.com/1.1/application/rate_limit_status.json')

        decoder = requisicao[1].decode()

        obj = json.loads(decoder)
        requests_faltando = obj['resources']['followers']['/followers/list']['remaining']
        statuses_update_remaining = obj['resources']['drafts']['/drafts/statuses/update']['remaining']
        statuses_update_limit = obj['resources']['drafts']['/drafts/statuses/update']['limit'] 
        statuses_update_reset = obj['resources']['drafts']['/drafts/statuses/update']['reset']
        hora_para_reset = statuses_update_reset / 3600
        min_para_reset = statuses_update_reset / 60
        seg_para_reset = statuses_update_reset
        print(f'Requests: faltam {requests_faltando}')
        print(f'Satus Update: {statuses_update_remaining}/{statuses_update_limit} Falta {hora_para_reset}h {min_para_reset}m {seg_para_reset}s')
        time.sleep(1)


def twittar(texto):
    nfoto = randint(0,52)
    print(f'Numero da foto: {nfoto}')
    api.update_with_media(f'./Fotos/{nfoto}.jpg', texto)


def start():
    while True:
        try:
            print('Verificando De novo...')
            requisicao = client.request('https://api.twitter.com/1.1/followers/list.json?count=200')

            decoder = requisicao[1].decode()

            obj = json.loads(decoder)
            # print(obj['users'][0]['screen_name'])
            followers = obj['users']
            total_de_folowers = getFollowersNow()
            #print(f'Total de folowers = {total_de_folowers}')

            print(f'Total de folowers : {total_de_folowers}')

            print('--- Verificando folowers novos...')

            for x in range(0,20):
                nome_do_seguidor = followers[x]['screen_name']
                if not nome_do_seguidor in getFollowersJson():
                    twittar(f'Obrigado @{nome_do_seguidor} por me seguir :)')
                    addUser(nome_do_seguidor)
                    print(f'@{nome_do_seguidor} Começou a seguir o BOT')
                    print(f'{x}/20')
                    time.sleep(5)

            getRequests()
            print('Aguardando mais um minuto...')
        except tweepy.error.TweepError as tpe:
            print(f'ERROR: {tpe}')
            print('ERROR: trying again...')   
        time.sleep(61)

def debug():
        requisicao = client.request('https://api.twitter.com/1.1/followers/list.json?count=200')

        decoder = requisicao[1].decode()

        obj = json.loads(decoder)
        # print(obj['users'][0]['screen_name'])
        followers = obj['users']
        total_de_folowers = int(len(followers))
        print('Total :', total_de_folowers)

        for x in range(total_de_folowers):
            follower = followers[x]['screen_name']
            addUser(follower)
        print('Seguidoes adicionados a database com sucesso!')

def getFollowersNow():
    follower_count = api.get_user('focacharmosa').followers_count
    return follower_count

#start()
getRequests()




