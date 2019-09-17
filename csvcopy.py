from selenium import webdriver
import click
data ='NIFTY 500'
fromDate = input('Enter starting date: ')
toDate = input('Enter last date : ')

driver = webdriver.Chrome("/home/amit/Downloads/chromedriver")
driver.get('https://www.nseindia.com/products/content/equities/indices/historical_index_data.htm')

data_box = driver.find_element_by_id('indexType')
data_box.send_keys(data)

start_box = driver.find_element_by_id('fromDate')
start_box.send_keys(fromDate)

to_box = driver.find_element_by_id('toDate')
to_box.send_keys(toDate)

get_data_btn = driver.find_element_by_id('get')
# get_data_btn.submit()
get_data_btn.click()

#get_last_btn =driver.find_element_by_link_text('Download file in csv format')
# get_last_btn =driver.findElement(By.linkText("Download file in CSV formate"))
# get_last_btn.click()
get_last_btn = driver.find_element_by_class('download-data-link')
# get_data_btn.submit()
get_data_btn.click()