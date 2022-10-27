from cgitb import text
from email.mime import audio
import requests
from bs4 import BeautifulSoup as bs
import fnmatch
import tqdm
import sqlite3

conn = sqlite3.connect('Online Audio Database.db')
c = conn.cursor()


url = 'https://downloadming.ws/bollywood-mp3-songs-a-to-z-list'


def Alphabet_URL():
    alphabet = []
    page = requests.get(url)
    soup = bs(page.text,'lxml')
    for link in soup.find_all('a'):
        link = link.get('href')
        if fnmatch.fnmatch(link,"*bollywood-mp3-songs?ap=*"):
            #print(link)
            alphabet.append(link)
    return alphabet


def Album_URL(url):
    album = []
    page = requests.get(url)
    soup = bs(page.text,'lxml')
    for link in soup.find_all('a'):
        link = link.get('href')
        if fnmatch.fnmatch(link,'*-mp3-songs'):
                #print(link)
                album.append(link)
    return album


def Audio_URL(url):
    audio = []
    page = requests.get(url)
    soup = bs(page.text,'lxml')
    for link in soup.find_all('a'):
        link = link.get('href')
        if fnmatch.fnmatch(link,'*320*.mp3'):
            #print(link)
            audio.append(link)    
    return audio


class Name:
    def __init__(self,text):
        self.text = text

    def Audio(self):
        texts = self.text.split('/')[-1]
        new_texts = texts.replace('%20', ' ')
        return new_texts
 

def Update_Database():
    for i in tqdm.tqdm(Alphabet_URL()):
        for h in tqdm.tqdm(Album_URL(i)):
            for j in Audio_URL(h):
                #print(j)
                #name = Name(j)
                #print(f'Audio: {name.Audio()}')
                pass

'''
url = 'https://new.dming2022.xyz/2016a/bollywood%20mp3/A%20Flying%20Jatt%20(2016)2/A%20Flying%20Jatt%20(2016)%20(320%20Kbps)/01%20-%20A%20Flying%20Jatt%20-%20Title%20Track%20-%20DownloadMing.SE.mp3'
name = Name(url)
print(f'Album: {name.Album()}\nYear: {name.Year()}\nAudio: {name.Audio()}')'''