from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def follow_page_followers(pagename, n):
	#####OPENS INSTAGRAM
	#INPUT YOUR PATH TO FIREFOX.EXE
	#THIS PATH FOR ME LOOKS LIKE THIS: 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
	binary = r'your path to firefox.exe'
	options = Options()
	options.binary = binary
	
	#INPUT YOUR PATH TO WEBDRIVER/ IN THIS CASE GECKODRIVER
	#FOR ME THIS LOOKS LIKE: "C:\\Users\\my user name\\Desktop\\gecko\\geckodriver.exe"
	browser = webdriver.Firefox(firefox_options=options, executable_path="your path")
	browser.implicitly_wait(5)
	browser.get('http://instagram.com/')

	#####LOGS IN AND GETS YOU PAST THE 'SAVE PASSWORD' AND 'TURN ON NOTIFICATIONS' PROMPTS
	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")
	
	#INPUT YOUR USERNAME AND PASSWORD BELOW
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
			#BROWSER.QUIT IS THE FUNCTION THAT CLOSES THE WEBPAGE
			browser.quit()
			break
		else:
			try:
				#CLICKS FOLLOW ON A USER YOU ARE NOT FOLLOWING
				#THIS IS THE HTML CLASS FOR THE 'FOLLOW' BUTTON
				follow = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
				follow.click()
				
				#CHANGED IT TO 90 SECONDS FROM 10 BECAUSE IT HELPS THE BOT LOOK MORE HUMAN AND DOES NOT GET LIMITED
				time.sleep(90)
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
loop = 0
while True:		    
	
	#THIS IS WHERE YOU CHOOSE WHAT PAGES TO FOLLOW FROM AND HOW MANY OF THEIR FOLLOWERS YOU WISH TO FOLLOW
	
	#THE PAGE NAME THAT YOU ENTER HAS TO BE EXACTLY THE SAME AS THE TARGET USERS INSTA HANDLE
	
	x = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	time.sleep(600)
	y = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	time.sleep(600)
	z = follow_page_followers(pagename = 'name of page you wish to follow their users', n = 20)
	time.sleep(600)
	
	#PRINTS THE LOOP COUNT SO I CAN EASILY KEEP TRACK OF HOW MANY TIMES IT HAS RAN
	loop += 1
	print('')
	print("loop number = " + str(loop))
	print('')

	
	
	''' I have found that by adding the 90 second sleep between following people and ALSO adding a 600 second sleep AFTER following from all pages is the safest route.
	    Don't worry. It's still very effective and has helped me grow my instagram quickly.
	'''
