from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def follow_page_followers(pagename, n):
	#####OPENS INSTAGRAM
	#INPUT YOUR PATH TO FIREFOX.EXE
	binary = r'your path to firefox.exe'
	options = Options()
	options.binary = binary
	#INPUT YOUR PATH TO WEBDRIVER/ IN THIS CASE GECKODRIVER
	browser = webdriver.Firefox(firefox_options=options, executable_path="your path")
	browser.implicitly_wait(5)
	browser.get('http://instagram.com/')

	#####LOGS IN AND GETS YOU PAST THE 'SAVE PASSWORD' AND 'TURN ON NOTIFICATIONS' PROMPTS
	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")
	username_input.send_keys("your username")
	password_input.send_keys("your password")

	#THIS IS THE HTML CLASS FOR THE LOG IN BUTTON
	login_button = browser.find_element_by_xpath("//button[@type='submit']")
	login_button.click()
	time.sleep(3)

	#THIS IS THE HTML CLASS FOR THE 'NOT NOW' BUTTON
	not_now_button = browser.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
	not_now_button.click()
	time.sleep(2)

	#THIS IS THE HTML CLASS FOR THE 'NO NOTIFICATIONS' BUTTON
	no_notifications = browser.find_element_by_class_name("aOOlW.HoLwm ")
	no_notifications.click()
	time.sleep(2)

	#####SEARCHES FOR YOUR TARGET PAGE IN THE SEARCH BAR AND SELECTS THE FIRST OPTION
	#####MAKE SURE TO INCLUDE THE FULL PAGENAME SO IT IS THE FIRST OPTION

	#THIS IS THE HTML CLASS FOR THE SEARCH BAR
	search = browser.find_element_by_class_name('XTCLo.x3qfX')
	search.send_keys(pagename)
	time.sleep(1)

	#THIS IS THE HTML CLASS FOR THE FIRST OPTION THAT POPS UP
	page = browser.find_element_by_class_name('z556c')
	page.click()
	time.sleep(2)

	#####CLICKS ON THE FOLLOWERS BUTTON TO DISPLAY THE FOLLOWERS OF THE PAGE
	#####THIS IS THE HTML PATH TO CLICK ON THE FOLLOWERS PAGE
	page_followers = browser.find_element_by_xpath(f"//a[@href = '/{pagename}/followers/']")
	page_followers.click()

	
	count = 0
	while count<=n:
		#ONCE YOU FOLLOW N NUMBER OF PEOPLE IT CLOSES
		if count == n:
			browser.quit()
			break
		else:
			try:
				#CLICKS FOLLOW ON A USER YOU ARE NOT FOLLOWING
				#THIS IS THE HTML CLASS FOR THE 'FOLLOW' BUTTON
				follow = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
				follow.click()
				count+=1
				print(f'followed someone {count}')
				try:
					#THIS CHECKS TO SEE IF AN OPTION TO UNFOLLOW POPS UP
					#AND IF SO, CLICKS THE 'CANCEL' BUTTON
					#THIS IS THE HTML CLASS FOR THE CANCEL BUTTON
					cancel = browser.find_element_by_class_name('aOOlW.HoLwm')
					cancel.click()
				except:
					pass
			except: 
				#SCROLLS DOWN UNTIL IT SEES A FOLLOW BUTTON
				#THIS IS THE HTML PATH TO THE SCROLLABLE FOLLOWERS LIST
				fBody  = browser.find_element_by_xpath("//div[@class='isgrP']")
				scroll = 0
				print('scrolling')
				while scroll < 2: # scroll 2 times
				    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
				    time.sleep(2)
				    scroll += 1

while True:		    
	#THIS HERE FOLLOWS 20 PEOPLE FROM EACH PAGE EVERY HOUR
	#THIS IS A SAFE LIMIT SO YOU ARE NOT LIMITED BY INSTAGRAM

	''' IN THIS CASE, I WILL PUT IN THREE SEPERATE ACCOUNTS AND FOLLOW 20 USERS FROM EACH TARGET ACCOUNT
		YOU CAN DO THIS FOR AS MANY ACCOUNTS AS YOU WOULD LIKE SO LONG AS YOU ONLY TOTAL UP TO 60 PER HOUR'''

	x = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	y = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	z = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	
	#SLEEP FOR 1 HOUR
	time.sleep(3600)
