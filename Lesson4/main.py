from time import time, sleep
import datetime as dt
import requests
import json


# start = time()
# for itm in range(10):
#     print(itm)
#     sleep(1)
# end = time()

#print(end - start)


response = requests.get('https://google.com')

print(response.text)