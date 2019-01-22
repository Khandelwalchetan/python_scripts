from selenium import webdriver
from getpass import getpass


usr=input("Enter the email id:  ")
pwd=getpass("Enter the password: ")

chromedriver=r"C:\Users\Chetan\Downloads\chromedriver_win32\chromedriver.exe"
browser=webdriver.Chrome(chromedriver)
browser.get('https://www.facebook.com/')

username_box=browser.find_element_by_id('email')
username_box.send_keys(usr)

pwd_box=browser.find_element_by_id('pass')
pwd_box.send_keys(pwd)

login_btn=browser.find_element_by_id("u_0_3")
login_btn.submit()





