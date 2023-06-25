from ipserver import IpServer
from database import DataBase
import json
from time import time

if __name__ == '__main__':
    cfg = None # system configs
    with open("configs.json",'r') as f:
        cfg = json.load(f)

    srv = IpServer("localhost",5000)
    db = DataBase()
    db.refresh()
    lastRefresh = time()  

    while True:
        request = srv.accept()
        currentTime = time()
        
        # check for auto refresh need
        if currentTime - lastRefresh > cfg["auto refresh"]*3600: # the config is in hour unit
            db.refresh()
            lastRefresh = currentTime

        # check for allowed refresh request 
        if "refresh" in request:
            if currentTime - lastRefresh > cfg["refresh gap"]*60: # the config is in miniut unit
                db.refresh()
                lastRefresh = currentTime
                srv.response("refresh succeded")
            else:
                srv.response("refresh failed")

        # apply filter to the current state
        if "filter" in request:
            srv.response(db.filter(request["filter"]))
