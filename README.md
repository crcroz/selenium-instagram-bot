# Selenium Bot to Follow a Users Followers

I was unable to get InstaPy to work for me, so after a lot of struggling, I decided to make selenium work for me. It worked quite nicely. It works decently


### The Basics of How It Works

* It logs onto Instagram for you, and searchs in the seach bar for your target page. 
* After getting to the page, it clicks on the followers pop up and starts following people.
* The hard part was getting it to scroll down in the pop up window and not the main page behind it.
* Because of this it does look a little strange when you watch it work, rest assured, it does work.

### Some Recent Changes
  I have added a 90 second sleep delay after following someone. This seems like a long time but trust me in the long run it is effective.
  I have also done away with an hour sleep time after cycling through pages, and opted for a 10 minute sleep time between switching pages.
  Both of these things have kept me from gettng limited by Instagram.
* If you do the math, by following 20 people  from 3 different pages, all with 10 minute sleep delay between them.. you can follow 720 people in a day.
    That is huge.
   It is possible to follow 60 people from one target user, and then sleep for the 600seconds. But I do not recommend following more than that
   before having it take a break. All about making it look more human.
    
    
### Things You Need To Make This Work:
  Gecko driver.
  https://github.com/mozilla/geckodriver/releases
  
  This bot only works with Firefox!
  
  Selenium
  https://selenium-python.readthedocs.io/installation.html
  
  
 ### Other
  So one problem I have noticed is that it will follow someone even if they have a private account. 
  
  What this means is, that as long as that one private account keeps denying you to follow them, you will keep hitting follow everytime they pop up as 
  your target page's follower.
  
  I had one guy message me saying I had requested to follow him 12 times.
  I just told him that he needed to keep my follow request active and not deny or confirm it, because the bot skips people you have requested.
  
  ### Last Thing
    Hopefully this goes without saying at this point, you cannot let this bot follow 3,000 people in one day. Instagram would probably shut down your account.
    
 # Selenium Bot to Unfollow Users Who Are Not Following You
  * First: Make sure you have both the who_follows_me and who_am_i_following scripts downloaded
  * Second: Run the Purge
  
  It works by simply getting your followers and getting who you are following.
  Then turns that into the accounts that are not following you back.
  It goes to each user page individually and unfollows them 1 by 1.
  
  ## Notes on the Purge
  You can only unfollow about 150 pages per day which is what the code is set to stop at.
  If you do get limited, you may be banned from unfollowing people for a few days.
  This has happened to me a few times which is why I slowed it down so much.
  
  
  





