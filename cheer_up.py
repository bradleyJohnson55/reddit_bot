import praw
import config
import time
import random 
import prawcore
import kitten_pics

BLACKLIST = {"suicidewatch", "depression", "petloss", "cats"}

def botLogin():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "cheer_up_bot")
	return r

def reply(comment, str): # str = trigger
	try:
		if comment.author.name != "cheer_up_bot" and comment.subreddit.display_name.lower() not in BLACKLIST:
			kittenPic = kitten_pics.kittenList[random.randint(0, kitten_pics.kittenListSize)]
			comment.reply('>' + str +"\n\n[Here is a picture of a kitten to cheer you up](" + kittenPic + ")")
			print ("\nsad person found -> " + comment.body)
			time.sleep(3)
	except Exception as e:
		print ('\n*******error*******\n')

def runBot(r):
	subreddit = r.subreddit('all')
	comments = subreddit.comments(limit = 100)
		
	for comment in comments:
		if ":(" in comment.body:
			reply(comment, ':(')
		elif ":'(" in comment.body:
			reply(comment, ":'(")
		elif "i feel sad now" in comment.body:
			reply(comment, "i feel sad now")
		elif "i'm sad " in comment.body:
			reply(comment, "i'm sad ")
		elif "i am sad " in comment.body:
			reply(comment, "i am sad")
	
	print ("\n...")
	time.sleep(2)

login = botLogin()
print ("entering reddit and grabbing 100 most recent comments....\nsearching for sad people")

while True:
	runBot(login)

