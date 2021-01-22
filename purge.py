from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import who_follows_me
import who_am_i_following

following = who_am_i_following.who_am_i_following()
followers = who_follows_me.who_follows_me()

unfollow = [user for user in following if user not in followers]

purge = [user.replace("'","") for user in unfollow]




def purge_following():
	#OPENS INSTAGRAM
	#INPUT YOUR PATH TO FIREFOX.EXE
	binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
	options = Options()
	options.headless = True 
	options.binary = binary
	#INPUT YOUR PATH TO WEBDRIVER/ IN THIS CASE GECKODRIVER
	browser = webdriver.Firefox(firefox_options=options, executable_path="your path here")
	browser.implicitly_wait(5)
	browser.get('http://instagram.com/')

	#LOGS IN AND GETS YOU PAST THE 'SAVE PASSWORD' AND 'TURN ON NOTIFICATIONS' PROMPTS
	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")
	username_input.send_keys("your username")
	password_input.send_keys("your password")

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
	
	x = 0
	while x <= 30:
	
		for user in purge:
			search = browser.find_element_by_class_name('XTCLo.x3qfX')
			search.send_keys(user)
			
			time.sleep(1)
      
			try:
				page = browser.find_element_by_class_name('z556c')
				page.click()
				time.sleep(2)
			except:
				search.clear()
			try:
				following_button = browser.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P')
				following_button.click()
				time.sleep(1)

				unfollow_button = browser.find_element_by_class_name('aOOlW.-Cab_')
				unfollow_button.click()
				x += 1
				print(f'unfollowed a nerd #{x}')
				time.sleep(90)
				if x %30== 0:
					print('unfollowed 30 more people')
					time.sleep(1200)
				if x == 150:
					return 'done'

			except:
				pass
				

the_purge = purge_following()
