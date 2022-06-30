import os,requests,sys
url = str(sys.argv)
x = requests.get(url)
print(x.text)
