import requests 
from bs4 import BeautifulSoup 
import re
 
url = requests.get("https://www.books.com.tw/web/sys_saletopb/books/")   
soup = BeautifulSoup(url.text,"html.parser") 
a = []


for i in soup.find_all('a',href = re.compile('[?]loc=P_0003_(\d+)')):
    a.append(i.text+':'+i['href'])
    #print(a)    

a = ''.join(a)        
with open('a.txt','w',encoding="utf-8") as f: 
    f.write(a)
    
