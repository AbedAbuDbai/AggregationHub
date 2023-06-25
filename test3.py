from ipclient import IpClient

if __name__ == '__main__':
    client = IpClient("localhost",5000)
    response = client.request({"refresh":"all"})
    print(response)
    response = client.request({"filter":{"Provider":6111, "STATUS": "Open"}})
    print(response)