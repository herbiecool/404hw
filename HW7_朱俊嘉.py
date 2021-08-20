from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

browser.get('https://tw.eztable.com/search?country=tw&date=2021-08-22&people=2&searchTab=restaurant&source=mobile.eztable.com&utm_campaign=branding_keyword&utm_medium=cpc&utm_source=marketing')

time.sleep(3)

for i in range(19):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(0.5)
        
soup = BeautifulSoup(browser.page_source,'html.parser') 
 
a = []
b = []
c = 0
    
for i in soup.find_all('h4',class_='sc-fHxwqH iaYcsX'):
    productname = i.text
    #print(productname)
    a.append(productname)
    c += 1
    
for i in soup.find_all('span',class_="sc-eIHaNI bvDXCA"):
    price = i.text
    #print(price)
    b.append(price)
    
keys = a
values = b
dic = dict(zip(keys,values))

print(dic)
#print(a)
#print(b)
print(c)

   
        