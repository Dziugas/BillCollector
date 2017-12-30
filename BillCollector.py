import os
import pdfkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#creates folder for receipt download
#folder = input('Please enter the name of the Folder where you want to keep your receipts. The folder will be located on the Desktop')
#os.makedirs(r'C:\Users\User\Desktop\%s'%folder)


#opens Linkedin
driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/payments/purchasehistory?trk=premium_manage_account_view_payment_history')

#opens the login form
signElement = driver.find_element_by_class_name('sign-in-link')
signElement.click()

#fills the login in form
emailElement = driver.find_element_by_id('session_key-login')
emailElement.click()
emailElement.send_keys('******@gmail.com')

passElement = driver.find_element_by_id('session_password-login')
passElement.click()
passElement.send_keys('*********')

#clicks to login
loginElement = driver.find_element_by_id('btn-primary')
loginElement.click()

#closes the cookie alert
cookieElement = driver.find_element_by_id('dismiss-alert')
cookieElement.click()

#waits and finds the receipt element, clicks it to open
element1 = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.CLASS_NAME, 'view-receipt'))
    )

latestReceiptElement = driver.find_element_by_class_name('view-receipt')
latestReceiptElement.click()

#finds the receipt section/dialog body from the pop up window
#receiptElement = driver.find_element_by_id('receipt')






#prints the page to pdf - but this does not let it sign up to LinkedIn
#url = driver.current_url
#print(url)
#pdfkit.from_url(url, 'out.pdf')


#waits and finds the print button element
#element2 = WebDriverWait(driver, 5).until(
#EC.presence_of_element_located((By.ID, 'print-button'))
#   )
#element2.click()

