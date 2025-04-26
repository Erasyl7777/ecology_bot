import requests
import random
def plast_util():    
    url = 'https://himstab.ru/info/articles/vtorichnaya-pererabotka/pererabotka-plastika/'
    res = requests.get(url)
    data = res.json()
    return data['url']


def plastik_zamena():    
    url = 'https://style.rbc.ru/health/5ce6394f9a79476f848aa883'
    res = requests.get(url)
    data = res.json()
    return data['url']


def plast_2gis():    
    url = 'https://2gis.kz/astana/search/%D0%BF%D1%80%D0%B5%D0%BC%20%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0?m=71.936649%2C51.16489%2F9.24'
    res = requests.get(url)
    data = res.json()
    return data['url']


def metall():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

