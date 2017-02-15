from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(login_url,username,password):
    driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(login_url)
    driver.implicitly_wait(20)
    username_element=driver.find_element(By.ID,"form:username_admin")
    username_element.send_keys(username)
    password_element=driver.find_element(By.ID,"form:password_admin")
    password_element.send_keys(password)
    login_element=driver.find_element(By.ID,"form:btn")
    login_element.click()
    return driver


def login_test(login_url,username,password,welcome_url):
    driver=login(login_url,username,password)
    time.sleep(5)
    current_url=driver.current_url
    if current_url == welcome_url:
       driver.quit()
       return "Pass"
    else:
        driver.quit()
        return "Fail"


def logout_test(login_url,username,password):
    driver = login(login_url, username, password)
    time.sleep(5)
    logout_menu=driver.find_element(By.ID,"logoutform:j_idt15_menuButton")
    logout_menu.click()
    logout=driver.find_element(By.XPATH,"//*[@id='logoutform:j_idt20']/span[2]")
    logout.click()
    time.sleep(5)
    current_url = driver.current_url

    if current_url == login_url:
       driver.quit()
       return "Pass"
    else:
        driver.quit()
        return "Fail"




def create_user(login_url,username,password,new_username,new_password):
    driver = login(login_url, username, password)
    time.sleep(5)
    general_menu=driver.find_element(By.XPATH,"//*[@id='adminForm:adminMenu']/div[1]/h3/span")
    general_menu.click()
    user_menu=driver.find_element(By.XPATH,"//*[@id='adminForm:j_idt33']/span[1]")
    user_menu.click()
    user_add=driver.find_elemnt(By.XPATH,"//*[@id='form:userslist:addNewUser']")
    user_add.clcik()
    username_field=driver.find_element(By.XPATH,"//*[@id='adduser_form:userName']")
    username_field.send_keys("Test")
    full_user_name=driver.find_element(By.XPATH,"//*[@id='adduser_form:userFullName']")
    full_user_name.send_keys("Test")
    password_field=driver.find_element(By.XPATH,"//*[@id='adduser_form:userPassword']")
    password_field.send_keys("Rakesh123!@")
    confirm_passsword=driver.find_element(By.ID,"adduser_form:confirmUserPassword")
    confirm_passsword.send_keys("Rakesh123!@")
    create_user=driver.find_element(By.XPATH,"//*[@id='adduser_form:btn']")
    create_user.click()





