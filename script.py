from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os.path
from os import path
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
def checklogin():
	try:
	    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((
	        By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]'
	    )))
	    return True
	except:
	    return False
print(style.GREEN+style.BOLD+"""
 __        ___           _                         
 \ \      / / |__   __ _| |_ ___  __ _ _ __  _ __  
  \ \ /\ / /| '_ \ / _` | __/ __|/ _` | '_ \| '_ \ 
   \ V  V / | | | | (_| | |_\__ \ (_| | |_) | |_) |
    \_/\_/  |_| |_|\__,_|\__|___/\__,_| .__/| .__/ 
                                      |_|   |_|    """+style.RESET)
print("""   ___       ____     _  __           __             _____ ____         
  / _ )__ __/ / /__  / |/ /_ ____ _  / /  ___ ____  / __(_) / /____ ____
 / _  / // / /  '_/ /    / // /  ' \/ _ \/ -_) __/ / _// / / __/ -_) __/
/____/\_,_/_/_/\_\ /_/|_/\_,_/_/_/_/_.__/\__/_/   /_/ /_/_/\__/\__/_/   
                                                                        
""")
print(style.BOLD+style.YELLOW+"[+]GITHUB : https://github.com/Eljakani"+style.RESET)
print(style.BOLD+"[+]Starting Web Client ..."+style.RESET)
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://web.whatsapp.com/")
while(not checklogin()):
	print(style.BOLD+"[+]Scan the QR Code to continue"+style.BOLD)
	try:
	    WebDriverWait(driver, timeout=50).until(EC.presence_of_element_located((
	        By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]'
	    )))
	    print(style.BOLD+style.GREEN+"=> Successfully logged in"+style.RESET)
	except:
	    print(style.BOLD+style.RED+"=> You aren't logged in"+style.RESET)
def checknumber(number):
	driver.get("https://web.whatsapp.com/send?phone="+number+"&text&app_absent=0")
	try:
		WebDriverWait(driver, timeout=30).until(EC.presence_of_element_located((
		By.XPATH, '//*[@id="side"]'
		)))
		try:
			WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((
			By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[1]/div/div/span'
			)))
			return True
		except:
			return False
	except:
			return False
def progress(count, total, suffix=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)
	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
	sys.stdout.flush()
txtfile = False
while txtfile == False:
	txtfile_name=input(style.BOLD+"[+]Enter your numbers list path (txt) : "+style.RESET)
	txtfile=path.exists(txtfile_name)
my_file = open(txtfile_name, "r")
content_list ={x.replace("\n", "") for x in my_file.readlines()} 
total=len(content_list)
working=0
print(style.BOLD+"=> Your list ["+style.YELLOW+txtfile_name+style.RESET+style.BOLD+"] contains "+style.YELLOW+str(total)+style.RESET+style.BOLD+" number")
for idx, val in enumerate(content_list,start=1):
	progress(idx, total, suffix='Checking : ['+val+'] | Valid  : ['+str(working)+']')
	if checknumber(val):
		working+=1
		file_object = open('valid.txt', 'a')
		file_object.write(val+"\n")
		file_object.close()
print("\nThe valid numbers are saved in 'valid.txt'")
