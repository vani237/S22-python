import requests

# resp = requests.get("http://google.com")

# s_code = resp.status_code
# #print(s_code)
# if resp.status_code == 200:
#     isUp = True
# else:
#     isUp = False

# print(isUp)        

urls = ['http://google.com', 'http://netflix.com','http://wikipedia.com', 'http://amazon.com']
for link in urls:
    resp = requests.get(link)
    if resp.status_code == 200:
        print(f"{link} is up")
    else:
        print(f"{link} is down")    