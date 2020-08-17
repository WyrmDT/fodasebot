# -*- coding: utf-8 -*-
import random, os, sys
import tweepy
from datetime import datetime

text_file = open("palavras.txt", "r")       #Abrimos a lista de palavras
palavras = text_file.readlines()        #E convertemos numa lista

consumer_secret = ""
consumer_key = ""           #Credencias do twitter dev
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 

numero = int(palavras[0])  #A palavra atual esta salvo no indice 0 da lista

texto = ""

if str(palavras[numero])[0] == '0':
    texto = "Fodase "+palavras[numero][1].lower()+"... Melhor não deixa quieto"
    #Algumas palavras não podem ser chingadas, marcamos elas com um 0
    #O bot so vai postar a primeira letra delas
    
else:
    texto = "Foda-se " + palavras[numero].lower() 
    #Caso não seja uma palavra marcada o bot manda ela se foder msm

    
api.update_status(status=texto) #Então postamos no twitter o texto gerado

palavras[0] = str(numero + 1) + '\n'     #Incrementos o contador

with open('palavras.txt', 'w') as file:
    file.writelines(palavras)       #E salvamos devolta no arquivo

#RESPONDENDO O @AmeTudo_Bot#

#Primeiro pegamos o dia atual#
hoje = datetime.today().strftime('%Y-%m-%d')

for tweet in tweepy.Cursor(api.user_timeline,
    since=hoje,
    screen_name='AmeTudo_Bot').items(2):  #Percorrendo todos o novos tweets
        if not tweet.retweeted: #Se não for um retweet ele avança
            if tweet.text.startswith("Amo"): #Se for um tweet que começa com "Amo" ele responde
                frase = tweet.text.split(" ")[1:] #pega a frase do tweet tirando o "Amo" do começo
                palavra = ""
                for w in frase[:-1]: #pega todo o resto menos o final que é um coração
                    palavra += w + " "  
                reply = f"*Foda-se {palavra}" #adiciona "Foda-se" no começo
                api.update_status(reply, tweet.id, auto_populate_reply_metadata=True) #responde o tweet