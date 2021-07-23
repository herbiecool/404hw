import requests 
from bs4 import BeautifulSoup 
 
url = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(url.text,"html.parser") 
lis = soup.find_all("li",class_='item') #書架上的書
divs = soup.find_all("div", class_="type02_bd-a") 
poo = [] 

for index,each_div in enumerate(divs): 
    h4 = each_div.find('h4') 
    
    if not h4: 
        print('h4') 
        continue 
    a = h4.find('a') 
    
    if not a: 
        print('a') 
        continue 
    bookName = a.text 

    
    ul = each_div.find('ul',class_="msg")
    if not ul: 
        continue 

    li = each_div.find('li') 
    
    if not li: 
        continue 
    
    b = li.find("a") #作者
    author = b.text 
    i = index+1 
    poo.append(str(i)+"-"+bookName+"-"+author) 
    print("No. "+str(i)+ ":"+bookName+"-"+author) 
    
    if index == 49: 
        break 

lis = soup.find_all("li",class_="item") 
count = 0 
for each_li in lis[:50]: 
    img = each_li.find("img") 
    src = img['src']
    alt = img['alt'] 
    
    url = requests.get(src) 
    with open(poo[count]+".jpg",'wb') as f: 
        f.write(url.content) 
    count += 1
    