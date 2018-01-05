import urllib.request
import time
import random

// loop ten times
for i in range(10):
    // once url request
    req = urllib.request.urlopen("http://**.org/cgi/*.do?rid=*").read()

    // get a random number
    delay = random.randint(2, 10)

    // display information
    print(i, req, delay)

    // let the time postpone
    time.sleep(delay)
