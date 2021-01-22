from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random

def who_follows_me():
	#OPENS INSTAGRAM
	#INPUT YOUR PATH TO FIREFOX.EXE
	binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
	options = Options()
	options.headless = True
	options.binary = binary
	#INPUT YOUR PATH TO WEBDRIVER/ IN THIS CASE GECKODRIVER
  
  #MY PATH LOOKS LIKE "C:\\Users\\MY NAME\\Desktop\\gecko\\geckodriver.exe"
	browser = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\your user\\........\\geckodriver.exe")
	browser.implicitly_wait(5)
	browser.get('http://instagram.com/')

	#LOGS IN AND GETS YOU PAST THE 'SAVE PASSWORD' AND 'TURN ON NOTIFICATIONS' PROMPTS
	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")
  
  #YOUR USERNAME AND PASSWORD HERE
	username_input.send_keys("yourusername")
	password_input.send_keys("yourpassword")

	#THIS IS THE HTML CLASS FOR THE LOG IN BUTTON
	login_button = browser.find_element_by_xpath("//button[@type='submit']")
	login_button.click()
	time.sleep(5)

	#THIS IS THE HTML CLASS FOR THE 'NOT NOW' BUTTON
	not_now_button = browser.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
	not_now_button.click()
	time.sleep(5)

	#THIS IS THE HTML CLASS FOR THE 'NO NOTIFICATIONS' BUTTON
	no_notifications = browser.find_element_by_class_name("aOOlW.HoLwm ")
	no_notifications.click()
	time.sleep(5)
  
  #THIS GETS YOU TO YOUR HOME PAGE
  
  #PUT YOUR EXACT USERNAME IN HERE
	my_page = browser.find_element_by_xpath("//a[@href = '/YOUR EXACT INSTAGRAM HANDLE/']")
	my_page.click()
	time.sleep(4)

	#CLICKS ON THE FOLLOWERS BUTTON TO DISPLAY YOUR FOLLOWERS
	#THIS IS THE HTML PATH TO CLICK ON THE FOLLOWERS PAGE
  
  #PUT YOUR EXACT USERNAME IN HERE
	page_followers = browser.find_element_by_xpath("//a[@href = '/YOUR EXACT INSTAGRAM HANDLE/followers/']")
	page_followers.click()
	
	#SCROLL TO BOTTOM OF FOLLOWER LIST
	fBody  = browser.find_element_by_xpath("//div[@class='isgrP']")
	scroll = 0
	
  #I FOUND THAT 850 SCROLLS PER 1000 FOLLOWERS WORKS WELL
	while scroll < 850: # scroll 5 times
		browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
		n = random.randint(0,21)
		if n == 10:
			time.sleep(2)
		scroll += 1

	#GET THEM FOLLOWERS BOOIIIIIIIIIIIII
  #THIS FINDS ALL OF THE USERNAMES OF YOUR FOLLOWERS
	usernames = browser.find_elements_by_css_selector('a.FPmhX.notranslate._0imsa')
	followers = [users.text for users in usernames]
	return followers
