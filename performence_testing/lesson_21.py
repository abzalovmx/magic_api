from turtledemo.penrose import start
import requests
from datetime import datetime

start = datetime.now()

response = requests.get('http://10.50.50.160:9222/ibs/index.jsp', verify=False)
print(response)

end = datetime.now()
print(end - start)