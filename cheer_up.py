import praw
import config
import time
import random 
import prawcore

BLACKLIST = {"suicidewatch", "depression"}


def botLogin():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "cheer_up_bot")
	return r

#if changing kittenList, don't forget to adjust kittenListSize
kittenList = ['http://freshpet.com/wp-content/uploads/2015/04/kitten.jpg', 
'http://upshout.net/wp-content/uploads/2015/06/dwarf-kitten-01.jpg', 'https://assets3.thrillist.com/v1/image/2563373/size/tmg-article_tall;jpeg_quality=20.jpg',
'https://img.buzzfeed.com/buzzfeed-static/static/2014-11/4/15/enhanced/webdr03/longform-original-29174-1415133936-9.jpg?downsize=715:*&output-format=auto&output-quality=auto',
'https://www.vets4pets.com/_resources/assets/inline/full/0/236990.jpg', 'http://cdn3-www.cattime.com/assets/uploads/2011/08/best-kitten-names-1.jpg',
'https://i.redd.it/x3kdiz7u9u2z.jpg', 'https://i.reddituploads.com/586cc251d1b94dbf9a685161b911eadf?fit=max&h=1536&w=1536&s=c4bad307b5767dde1b391fcc82cd126a',
'https://i.redd.it/yr01t7xz5rwy.jpg', 'https://i.redd.it/2af88hhk9dsy.jpg', 'https://i.redd.it/0tx76hl4v5ty.jpg']
kittenListSize = 10


def reply(comment, str): # str = trigger
	try:
		if comment.author.name != "cheer_up_bot" and comment.subreddit.display_name.lower() not in BLACKLIST:
			kittenPic = kittenList[random.randint(0, kittenListSize)]
			comment.reply('>' + str +"\n\n[Here is a picture of a kitten to cheer you up](" + kittenPic + ")")
			print ("\nsad person found -> " + comment.body)
			time.sleep(3)
	except Exception as e:
		print ('\n*******some sort of error*******\n')

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

	
	print ("\nno sad people found...sleeping 2 secs")
	time.sleep(2)

login = botLogin()
print ("entering reddit and grabbing 100 most recent comments....\nsearching for sad people")
while True:
	runBot(login)

