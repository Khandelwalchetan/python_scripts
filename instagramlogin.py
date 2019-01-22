from selenium import webdriver
from getpass import getpass

chromedriver=r"C:\Users\Chetan\Downloads\chromedriver_win32\chromedriver.exe"
browser=webdriver.Chrome(chromedriver)

browser.get("https://www.instagram.com/accounts/login/?hl=en")

fb_btn=browser.find_element_by_class_name("KPnG0")
fb_btn.click()

usr=input("Enter the email id:  ")
pwd=getpass("Enter the password: ")


username_box=browser.find_element_by_id('email')
username_box.send_keys(usr)

pwd_box=browser.find_element_by_id('pass')
pwd_box.send_keys(pwd)

login_btn=browser.find_element_by_id("loginbutton")
login_btn.submit()
