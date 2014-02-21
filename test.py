import requests

url='http://www.baidu.com'
r=requests.get(url)  
data=r.text             

print data
