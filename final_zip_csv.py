from selenium import webdriver
import click

driver = webdriver.Chrome("/home/amit/Downloads/chromedriver")


# DD = input(' Enter day: ')
# MM = input('Enter month: ')
# YYYY = input('Enter year : ')

DD ='04'
MM="Dec"
YYYY= "2018"

driver.get('https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx')

first_box = driver.find_element_by_id('ContentPlaceHolder1_rbtDeri')
first_box.click()

DD_box = driver.find_element_by_id('ContentPlaceHolder1_fdate1')
DD_box.send_keys(DD)

MM_box = driver.find_element_by_id('ContentPlaceHolder1_fmonth1')
MM_box.send_keys(MM)

YYYY_box = driver.find_element_by_id('ContentPlaceHolder1_fyear1')
YYYY_box.send_keys(YYYY)

get_submit_btn = driver.find_element_by_id('ContentPlaceHolder1_btnSubmit')
get_submit_btn.click()

get_zip_btn = driver.find_element_by_id('ContentPlaceHolder1_btnHylSearBhav')
get_zip_btn.click()