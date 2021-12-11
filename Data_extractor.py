from jina import Document
from jina.types.arrays.document import DocumentArray
from bs4 import BeautifulSoup
import requests
from jina import flow
url="http://www.housemd-guide.com/characters/houserules.php"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
quotes=[]
for row in soup.findAll("li"):
    s=str(row.text)
    try:
        a=s.index('"')
        b=s.index('"',a+1)
    except:
        continue
    s=s[a+1:b]
    quotes.append(s)
d=DocumentArray()
for row in quotes:
    d.append(row)
