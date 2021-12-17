from Data_extractor import quotes
from jina import Document,Flow,DocumentArray

docs=DocumentArray()
for i in range(len(quotes)):
    docs.append(Document(text=quotes[i]))
#converted list of strings to document array to be processed by jina
flow=(Flow()
.add(uses="jinahub://SpacyTextEncoder" ,name="Encoder" ,install_requirements=True)
.add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer"))

def index():
    with flow:
        flow.index(inputs=docs)
def search():
    with flow:
        query=Document(text=input("Enter search term: "))
        response=flow.search(inputs=query ,response=True)
        print("The matching quote is : ",response)


index()
print(docs)
while(True):
    x=input("Enter choice: 1.search 2. close \n")
    try:
        x=int(x)
    except:
        print("Wrong Input program terminated")
        break
    if x==2:
        break
    else:
        search()
