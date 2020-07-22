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
    requisicao = client.request('https://api.twitter.com/1.1/application/rate_limit_status.json')

    decoder = requisicao[1].decode()

    obj = json.loads(decoder)
    requests_faltando = obj['resources']['followers']['/followers/list']['remaining']
    #statuses_update_remaining = obj['resources']['drafts']['/drafts/statuses/update']['remaining']
    #statuses_update_limit = obj['resources']['drafts']['/drafts/statuses/update']['limit'] 
    #statuses_update_reset = obj['resources']['drafts']['/drafts/statuses/update']['reset']
    #hora_para_reset = statuses_update_reset / 3600
    #min_para_reset = statuses_update_reset / 60
    #seg_para_reset = statuses_update_reset
    print(f'Requests left: {requests_faltando}')
    #print(f'Satus Update: {statuses_update_remaining}/{statuses_update_limit} Falta {hora_para_reset}h {min_para_reset}m {seg_para_reset}s')
    time.sleep(1)


def tweet(texto):
    picture_number = randint(0,52)  #52 = number of pictures in 'Images' folder
    #print(f'Picture number: {nfoto}')
    api.update_with_media(f'./Images/{picture_number}.jpg', texto)


def start():
    while True:
        try:
            print('Checking again...')
            requisicao = client.request('https://api.twitter.com/1.1/followers/list.json?count=200')

            decoder = requisicao[1].decode()

            obj = json.loads(decoder)
            followers = obj['users']
            total_de_folowers = getFollowersNow()

            print(f'Followers count: {total_de_folowers}')

            print('--- Checking new followers ...')
            followers_waiting = 0

            for x in range(0,200):
                follower_name = followers[x]['screen_name']
                if not follower_name in getFollowersJson():
                    followers_waiting = followers_waiting + 1

            for x in range(0,200):
                follower_name = followers[x]['screen_name']
                if not follower_name in getFollowersJson():
                    followers_waiting = followers_waiting - 1
                    tweet(f'Obrigado @{follower_name} por me seguir :)') # 'Thank you @{follower_name}!
                    addUser(follower_name)
                    print(f'@{follower_name} is now following the BOT')
                    print(f'Position : {followers_waiting}')
                    time.sleep(5)

            getRequests()
            print('Waiting a minute...')
        except tweepy.error.TweepError as tpe:
            print(f'ERROR: {tpe}')
            print('ERROR: trying again...')  
            time.sleep(5 * 60) 
        time.sleep(61)

def addAllFollowersToJsonFile():
        requisicao = client.request('https://api.twitter.com/1.1/followers/list.json?count=200')

        decoder = requisicao[1].decode()

        obj = json.loads(decoder)
        followers = obj['users']
        total_de_folowers = int(len(followers))
        print('Total :', total_de_folowers)

        for x in range(total_de_folowers):
            follower = followers[x]['screen_name']
            addUser(follower)
        print('Followers successfully added!')

def getFollowersNow():
    twitter_acount_user = credentials.account_user
    follower_count = api.get_user(twitter_acount_user).followers_count
    return follower_count

start()




