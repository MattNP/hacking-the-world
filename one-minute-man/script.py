import requests
import time
from datetime import datetime

url = 'http://www.hacker.org/challenge/misc/minuteman.php'
response = requests.get(url).text[13:]
while "back later" in response:
    print("not yet")
    time.sleep(60)
    response = requests.get(url).text[13:]
file = open('solution.txt','w')
file.write((str(datetime.now()) + " " + response))
file.close()
