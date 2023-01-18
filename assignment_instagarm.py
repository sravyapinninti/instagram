from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time



class Instagram():

    def name_matching(self):

        url="https://www.instagram.com/"
        driver=webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        try :
            
            user_name=driver.find_element(By.XPATH,"//input[@name='username']").send_keys("sravya91p")#login_username
            
            driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Guvi@2022")#password
            

        except :

            print("please enter valid credentials")


        login=driver.find_element(By.XPATH,"//button[@type='submit']")
        login.click()    #login


        driver.find_element(By.XPATH,"//button[text()='Not Now']").click()
        driver.find_element(By.XPATH,"//button[text()='Not Now']").click()

        #message_tab
        wait=WebDriverWait(driver,10)
        message=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/direct/inbox/']"))).click()

        login_name=driver.find_element(By.XPATH,"//div[text()='sravya91p']").text

        #print(login_name)
        #driver.find_element(By.XPATH,"//input[@name='username']").get_attribute('value')

        a='sravya91p'

        if a==login_name:
            print("verified")
        else:
            print("please check credentials")


        #send_message

        driver.find_element(By.XPATH,"//button[text()='Send Message']").click()

        #input_name

        driver.find_element(By.XPATH,"//input").send_keys("sharmiladear")

        actions=ActionChains(driver)

        inputname=driver.find_element(By.XPATH,"//div[@class='_abm4']//button[@class='_abl-']")

        actions.move_to_element(inputname).perform()
        inputname.click()


        #next
        driver.find_element(By.XPATH,"//div[text()='Next']").click()

        #send_message

        message=driver.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
        message.send_keys("hi")
        
        #print(a)
        
        
        
        #send

        driver.find_element(By.XPATH,"//button[text()='Send']").click()
        time.sleep(8)

        text1=driver.find_element(By.XPATH,"//div[@class='_acd2 _acd3']").text
        print(text1)


        if a==text1:
            print("verified")
        else:
            print("check message")

        

        time.sleep(4)


    


a=Instagram()
a.name_matching()