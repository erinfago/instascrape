'''
Author: Erin Fago

Date: June 2020

Purpose: Returns a file fakefriends.txt that contains a list everyone that the entered account follows but does not follow them back.

'''

import time
import csv
import random
import math
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


#instagram account class and related functions
class gramBot():
	#initialization
	def __init__(self, username, password):
		self.browser = webdriver.Chrome('YOUR PATH HERE')
		self.username = username
		self.password = password

	#sign in and automatic window close
	def signin(self):

		self.browser.get("https://www.instagram.com/")

		time.sleep(4)

		#body where we will send username 
		usernameInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')

		#fill in info
		usernameInput.send_keys(self.username)

		#body where we will send username 
		passwordInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')

		#fill in info
		passwordInput.send_keys(self.password)

		time.sleep(4)

		#press enter
		passwordInput.send_keys(Keys.ENTER)

		print("Pressed enter ... logging in now...\n")
		
		time.sleep(8)

		#if it asks you to safe your log on info
		try:
			self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
		except: 
			print("")

		time.sleep(4)

		#if it asks to turn on notifications
		try:
			self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
		except:
			print("")

		time.sleep(4)

	#return a list of the user's followers
	def getUserFollowers(self):
		self.browser.get('https://www.instagram.com/' + self.username)
		time.sleep(2)
		followersLink = self.browser.find_element_by_css_selector('ul li a')
		followersLink.click()
		time.sleep(2)

		followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
		numloaded = len(followersList.find_elements_by_css_selector('li'))
		followersList.click()

		#find number of followers
		totfollow = self.browser.find_element_by_xpath("//li[2]/a/span").text
		

		totfollow = totfollow.replace(" ", "")
		totfollownum = int(totfollow)
		print("You have", totfollow, "people following you.")

		#scroll down the page and show progress
		while numloaded < totfollownum:
			self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followersLink)

			#varied pause time
			time.sleep(random.randint(500,1000)/1000)
		
			numloaded = len(followersList.find_elements_by_css_selector('li'))

			print("Extracting data [", end='')
			progress = (numloaded/totfollownum)*100
			progress = int(math.ceil(progress))
			restnum = 100-progress
			show = "|"*progress
			rest = " "*restnum
			print(show, end='')
			print(rest, end='' )
			print("]")


			scr1 = self.browser.find_element_by_xpath('/html/body/div[4]')
			self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)


		followers = []
		counter = 0
		
		for user in followersList.find_elements_by_css_selector('li'):
			# what number user we are on
			counter+= 1
			total = counter/numloaded

			print("Followers loading: ", total*100, "%")

			user = user.text
			userLinkList = user.split('\n')
			followers.append(userLinkList[0])
		print("Done with getting followers!")
		return followers
	
	#returns list of who the user follows
	def getUserFollowees(self):
		#exit out fo the followers window
		try:
			exitthis = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
		except:
			print("")

		time.sleep(2)

		#open following window
		followingLink = self.browser.find_element_by_xpath("//li[3]/a/span")
		followingLink.click()
		time.sleep(2)
		followingList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
		numloaded = len(followingList.find_elements_by_css_selector('li'))
		followingList.click()

		#find number of followers
		totfollowing = self.browser.find_element_by_xpath("//li[3]/a/span").text


		totfollowing = totfollowing.replace(" ", "")
		totfollowingnum = int(totfollowing)
		print("You are following ", totfollowing, " people.")


		#scroll down the page until all loaded and show progress
		while numloaded < totfollowingnum:
			self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followingLink)
			time.sleep(random.randint(500,1000)/1000)
			numloaded = len(followingList.find_elements_by_css_selector('li'))
			
			
			print("Extracting data [", end='')
			progress = (numloaded/totfollowingnum)*100
			progress = int(math.ceil(progress))
			restnum = 100-progress
			show = "|"*progress
			rest = " "*restnum
			print(show, end='')
			print(rest, end='' )
			print("]")

			
			scr1 = self.browser.find_element_by_xpath('/html/body/div[4]')
			self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

		

		following = []
		counter = 0

		#add each follower to list
		for user in followingList.find_elements_by_css_selector('li'):
			#tells us what number user we are on
			counter+= 1
			total = counter/numloaded

			print("Following loading: ", total*100, "%")


			user = user.text
			userLinkList = user.split('\n')
			following.append(userLinkList[0])
		print("Done with getting followers!")
		return following

	#writes to output file
	def theoutput(self, final):
		date_time = datetime.datetime.now()
		filename = "fakefriends" + date_time.strftime("%Y-%b-%d %H.s%M") + ".txt"
		fout = open(filename,"w")


		print("Output a list of people that do not follow you back to a file called fakefriends[datetime].txt! \n")
		for usr in final:
			fout.write(usr)
			fout.write("\n")

		fout.close()

	#compares the followers and following list and calls output function
	def compare(self, follower, following):
		final = []
		for usr in following:
			if usr not in follower:
				final.append(usr)

		self.theoutput(final)

	#closes browser and terminates any associated processes
	def closeBrowser(self):
		self.browser.quit()



def main():
	#create instance of user
	u_name = input("Please enter your username: ")
	p_word = input("Please enter your password: ")

	bot = gramBot(u_name, p_word)

	bot.signin()

	follower = bot.getUserFollowers()
	following = bot.getUserFollowees()
	bot.compare(follower, following)

	print("All done! Bye bye thank you!\n")
	
	bot.closeBrowser()


main()