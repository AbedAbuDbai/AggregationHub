from fake_fetch import FakeFetch

class DataBase:
    def __init__(self):
        self.banana = []
        self.strawberry = []
    
    def refresh(self):
        fetcher = FakeFetch()
        self.banana = fetcher.fetch('http://fakeurl/homeassignment/banana')
        self.strawberry = fetcher.fetch('http://fakeurl/homeassignment/strawberry')
    
    def filter(self, key2val:dict):
        aggregated = self.__aggregate__(key2val)
        return {"data": self.__extract__(aggregated)}

    def __aggregate__(self, key2val:dict):
        results = dict()
        for data,idPrefex in [(self.banana,'banana'),(self.strawberry,'strawberry')]:
            for case in data['data']:
                if self.__isMatch__(case, key2val):
                    aggregationKey = (case["Provider"],case["CREATED_ERROR_CODE"])
                    productAffected = case["PRODUCT_NAME"]
                    supportCase = (idPrefex,case["Case ID"])
                    value = results.get(aggregationKey,[set(),set()])
                    value[0].add(productAffected)
                    value[1].add(supportCase)
                    results[aggregationKey] = value
        return results

    def __extract__(self, aggregated):
        data = []
        for aggregationKey, value in aggregated.items():
            row = {"Error Code": aggregationKey[1], 
                    "Provider Name": aggregationKey[0],
                    "Products Affected": value[0],
                    "Number of support cases": len(value[1]),
                    "List of all support cases": value[1]}
            data.append(row)
        return data

    def __isMatch__(self, case:dict, key2val:dict):
        for key,val in key2val.items():
            if key in case and case[key]!=val:
                return False
        return True