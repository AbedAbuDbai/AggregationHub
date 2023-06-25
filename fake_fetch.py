import json

class FakeFetch:
    def fetch(self, url:str):
        if url=='http://fakeurl/homeassignment/banana':
            with open('banana.json','r') as f:
                return json.load(f)
        elif url=='http://fakeurl/homeassignment/strawberry':
            with open('strawberry.json','r') as f:
                return json.load(f)
        else:
            return {}