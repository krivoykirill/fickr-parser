#Simple assignment
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib.request import urlretrieve

globalLinkList = []

for i in range(1,2):

    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        driver.get('https://www.flickr.com/photos/18569154@N02/page'+str(i))
        driver.maximize_window()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(4)
        html = driver.page_source
        linkList = re.findall("/photos/18569154@N02/([a-zA-Z0-9]*)/",html)
        print(len(linkList))
        globalLinkList.extend(linkList)




for imageId in globalLinkList:
    if 'page' not in imageId:
        with webdriver.Chrome(ChromeDriverManager().install()) as driver:
            driver.get('https://www.flickr.com/photos/18569154@N02/'+str(imageId)+'/sizes/k')
            # src = driver.find_element_by_xpath("//div[@class='spaceball]//img").get_attribute("src")
            src = driver.find_element_by_css_selector('#allsizes-photo img').get_attribute("src")
            print(src)

            # download the image
            urlretrieve(src, "captcha"+str(imageId)+".png")
            
