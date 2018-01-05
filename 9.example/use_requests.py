import requests
import time
import random

// loop ten times
for i in range(10):
    // random an Ip address
    IP = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))

    // create the request headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.86 Safari/537.36',
        'X-Forwarded-For': IP,
        'CLIENT_IP': IP,
        'VIA': IP,
        'REMOTE_ADDR': IP
    }

    // declare a url
    url = 'http://***.org/cgi/*.do?rid=***'
    session = requests.Session()
    // once request
    res = session.get(url, headers = headers)

    // display information
    print(i + 1, res.cookies, IP, res.text)

    // waiting for ten minutes
    time.sleep(10)
