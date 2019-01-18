from selenium import webdriver


browser = webdriver.Chrome('D:\Download\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
browser.get('https://www.facebook.com')
email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
login_button = browser.find_element_by_id('loginbutton')
email.send_keys('#ourid')
password.send_keys('#yourpass')
login_button.click()


