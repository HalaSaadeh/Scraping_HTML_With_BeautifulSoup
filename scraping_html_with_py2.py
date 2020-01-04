
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position=input('Enter position ')
iter=input('Enter count')
position=int(position)
iter=int(iter)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retrieving:",url)
# Retrieve all of the anchor tags

while iter>0:
    pos=1
    tags = soup('a')
    for tag in tags:
        newurl=tag.get('href', None)
        name=tag.contents[0]
        if pos==position:
            break
        pos+=1
    html = urllib.request.urlopen(newurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving:",url)
    iter-=1

print(name)
