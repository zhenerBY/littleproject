import requests


class CatRequest():
    HOST_CATS = 'https://aws.random.cat/meow'

    def __init__(self):
        data = requests.get(CatRequest.HOST_CATS)
        json_data = data.json()
        self.url = json_data['file']
        self.ext = self.url.split('.')[-1]


class DoqRequest():
    HOST_DOGS = 'https://dog.ceo/api/breeds/image/random'

    def __init__(self):
        data = requests.get(DoqRequest.HOST_DOGS)
        json_data = data.json()
        self.url = json_data['message']
        self.ext = self.url.split('.')[-1]

