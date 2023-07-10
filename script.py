from requests_html import HTMLSession
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_urls():
    urls_1="https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060-oc-v2-12gb-9514.html"
    urls_2="https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060-oc-v2-12gb-9514.html"
    session= HTMLSession()
    record_session_1=session.get(urls_1)
    record_session_2=session.get(urls_2)
    buy_zone_1= record_session_1.html.find("#product-availability")
    buy_zone_2= record_session_2.html.find("#product-availability")
    return buy_zone_1, buy_zone_2


def check_availability(web_availability_1,web_availability_2):
    checking=True
    c=None
    while checking:
        availability_1=web_availability_1[0].text
        availability_2=web_availability_2[0].text
        if availability_1==availability_2:
            checking=False
            c=True
            return c
            
            
        else:
            sleep(30)
            values_urls=get_urls()    
            print(availability_2+'\n I am waiting for a stock, I tell you if the stock is ready.')

def main():
    values_urls=get_urls() 
    web_availability_1=values_urls[0]
    web_availability_2=values_urls[1]
    check_availability(web_availability_1,web_availability_2)
    f=True
    driver=webdriver.Chrome()
    # driver.get("https://www.neobyte.es/gigabyte-rtx-3060-windforce-oc-12gb-tarjeta-grafica-15076.html")
    driver.get('https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060-oc-v2-12gb-9514.html')
    sleep(6)
    
    value_driver=driver.find_element(By.CLASS_NAME,'btn.btn-primary.btn-lg.add-to-cart')
    value_driver.click()
    sleep(6)
    value_shop=driver.find_element(By.CLASS_NAME,'btn.btn-primary.btn-block.btn-lg.mb-2')
    value_shop.click()
    value_text=driver.find_element(By.NAME,'firstname')
    value_text.send_keys('Leonel')
    value_text_lastname=driver.find_element(By.NAME,'lastname')
    value_text_lastname.send_keys('Santana')
    value_text_email=driver.find_element(By.NAME,'email')
    print(value_text_email)
    sleep(6)
    value_text_email.send_keys('leonelsantana32@gmail.com')
    sleep(2)
    # value_text_email.
    # value_text_email.send_keys('leonelsantana32@gmail.com')
    # print(value_text_email)
    # value_text_password=driver.find_element(By.NAME,'password')
    # value_text_password.send_keys('Babylon182')
    value_text_birthday=driver.find_element(By.NAME,'birthday')
    value_text_birthday.send_keys('26/12/1998')

    privacy_customer=driver.find_element(By.ID,'ff_customer_privacy')
    privacy_customer.click()

    

    while f:
        if check_availability:
            pass
            
    

if __name__=='__main__':
    main()
