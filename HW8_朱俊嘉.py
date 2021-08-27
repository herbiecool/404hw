from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import requests

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

browser.get("https://cc0.wfublog.com/")
soup = BeautifulSoup(browser.page_source,'html.parser')
page = soup.find_all("div",class_='gsc-cursor-page')
time.sleep(0.5)
inputBar = browser.find_element_by_class_name("custom_search_box")
inputBar.send_keys("puppy")
time.sleep(0.5)
inputBar.send_keys(Keys.ENTER)

#def image():
   
for i in range(2):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(0.5)
    
for i in soup.find_all("a",class_='gs-image gs-image-scalable'):
    img = i.find("img")
    src = img['src'] 
    print(src)

    imgRespond = requests.get(src)
    with open('image'+'.jpg',"wb") as f:
        f.write(imgRespond.content)
'''
a = browser.find_element_by_name("div")
image()
for i in range(17):
    a.send_keys(Keys.TAB)
a.send_keys(Keys.ENTER)
image()
for i in range(9):
    for i in range(1):
        a.send_keys(Keys.TAB)
        a.send_keys(Keys.ENTER) 
        '''


'''
image()
page2 = browser.find_elements_by_class_name("gsc-resultsbox-visible")
page2.send_keys(Keys.ENTER)
image()
page3 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page3.send_keys(Keys.ENTER)    
image()
page4 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page4.send_keys(Keys.ENTER)
image()
page5 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page5.send_keys(Keys.ENTER)
image()
page6 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page6.send_keys(Keys.ENTER)
image()
page7 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page7")
page7.send_keys(Keys.ENTER)
image()
page8 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page8.send_keys(Keys.ENTER)
image()
page9 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page9.send_keys(Keys.ENTER)
image()
page10 = browser.find_elements_by_class_name("gsc-cursor-page gsc-cursor-current-page")
page10.send_keys(Keys.ENTER)
'''







