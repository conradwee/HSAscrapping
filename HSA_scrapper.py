
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as soup



class HSABot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
bot = HSABot()
bot.driver.get('https://eservice.hsa.gov.sg/medics/md/mdEnquiry.do?action=getAllDevices&_ga=2.183810082.563179921.1554083187-551332391.1551944793')
nxt_btn = bot.driver.find_element_by_xpath('//*[@id="page"]/form/table[3]/tbody/tr/td/table[4]/tbody/tr/td[2]/a[1]')
page_html = bot.driver.page_source
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("td",{"class":"fmLblCell2"})
out_filename = "HSA.csv"
f = open(out_filename, "w", encoding="utf-8")   
headers = "product_name\n"
f.write(headers)


for x in range(10):
    name = page_soup.findAll("a",{"class":"archorSpcSym"})
    product_name = name[x].text
 
   
    print(product_name)
    f.write(product_name + "\n")

for y in range(1830):
    nxt_btn = bot.driver.find_element_by_xpath("//*[contains(text(), 'next')]")
    nxt_btn.click()
    del page_html
    del page_soup
    del containers
    del name
    del product_name

    page_html = bot.driver.page_source
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("td",{"class":"fmLblCell2"})
    x = 0
    for x in range(10):
        name = page_soup.findAll("a",{"class":"archorSpcSym"})
        product_name = name[x].text
        print(product_name)
        f.write(product_name + "\n")
f.close()