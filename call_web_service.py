import json
import requests

    
url = 'http://172.188.9.245:5001/simpleAPI'
myobj = {'message_key': 'message_val',
         'Hello':'parames'}

x = requests.post(url, data = json.dumps(myobj))
