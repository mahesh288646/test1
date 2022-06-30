import os,requests,sys
url = str(sys.argv)
print(url)
x = requests.get(url)
print(x.text)
