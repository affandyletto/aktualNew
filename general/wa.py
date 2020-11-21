from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
from webdriver_manager.chrome import ChromeDriverManager


driver = None
Link = "https://web.whatsapp.com/"
wait = None

def tutup():
	driver.get("https://web.whatsapp.com/")
	driver.quit()

def whatsapp_login():
	global wait, driver, Link
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--user-data-dir=chrome-data")
	PATH="C:/pln/Program Aktual/aktual/chromedriver/chromedriver.exe"
	driver= webdriver.Chrome(PATH,options=chrome_options)
	wait = WebDriverWait(driver, 20)
	print("Scan QR Code ")
	driver.get(Link)
	driver.maximize_window()
	print("QR code berhasil di scan")

def send_message_to_unsavaed_contact(number,msg,count):
	# Reference : https://faq.whatsapp.com/en/android/26000030/
	params = {'phone': str(number), 'text': str(msg)}
	end = urllib.parse.urlencode(params)
	final_url = Link + 'send?' + end
	driver.get(final_url)
	WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
	try:
		sleep(3)
		wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button'))).click()
		
	except Exception as e:
		print("Nomor HP tidak ditemukan")

	msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	for index in range(count-1):
		msg_box.send_keys(msg)
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
	
	

def send_attachment_to_unsavaed_contact(number, file_name):
	print("In send_attachment_to_unsavaed_contact method")
	params = {'phone': str(number)}
	end = urllib.parse.urlencode(params)
	final_url = Link + 'send?' + end
	print(final_url)
	driver.get(final_url)
	WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
	print("Page loaded successfully.")
	try:
		sleep(3)
		wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]'))).click()		
	except Exception as e:
		print("Fail during click on Attachment button.")
		print("Nomor HP tidak ditemukan")
		driver.quit()

	attachment = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
	attachment.send_keys(file_name)
	sleep(5)
	send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
	send.click()
	print("File sent successfully.")

	
