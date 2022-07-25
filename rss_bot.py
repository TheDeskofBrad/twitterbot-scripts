#!/usr/bin/python
# -*- coding: utf-8 -*-

# Get RSS feed items from http://example.net/feed.xml and post to Twitter
# Based on original script by Peter Dalle - https://github.com/peterdalle/twitterbot/

from twython import Twython, TwythonError
import argparse, os, re, time, feedparser
from datetime import date

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--dry-run", help="show what would have been tweeted", action="store_true")
args = parser.parse_args()

# Settings for the application.
class Settings:
	# RSS feed to read and post tweets from
	FeedUrl = "https://thedeskofbrad.ca/index.xml"
	# Log file to save all tweeted RSS links (one URL per line)
	PostedUrlsOutputFile = os.path.dirname(__file__) + "/rss_bot.log"

# Twitter authentication settings
class TwitterAuth:
	ConsumerKey = os.environ['TWITTER_API_KEY']
	ConsumerSecret = os.environ['TWITTER_API_SECRET']
	AccessToken = os.environ['TWITTER_ACCESS_TOKEN']
	AccessTokenSecret = os.environ['TWITTER_ACCESS_SECRET']

# Post tweet to account
def PostTweet(title, link):
	# Truncate post title and append '...' at end if length exceeds 250 chars (which is enough space for a t.co link)
	title = (title[:250] + '...') if len(title) > 250 else title
	message = title + " " + link
	try:
		# Tweet message
		twitter = Twython(TwitterAuth.ConsumerKey, TwitterAuth.ConsumerSecret, TwitterAuth.AccessToken, TwitterAuth.AccessTokenSecret)
		twitter.update_status(status = message)
	except TwythonError as e:
		print(message)

# Has the URL already been posted?
def IsUrlAlreadyPosted(url):
	if os.path.isfile(Settings.PostedUrlsOutputFile):
		# Check whether URL is in log file
		f = open(Settings.PostedUrlsOutputFile)
		posted_urls = f.readlines()
		f.close()
		if (url + "\n" or url) in posted_urls:
			return(True)
		else:
			return(False)
	else:
		return(False)

# Mark the specific URL as already posted
def MarkUrlAsPosted(url):
	try:
		# Write URL to log file
		f = open(Settings.PostedUrlsOutputFile, "a")
		f.write(url + "\n")
		f.close()
	except:
		print("Write error:", sys.exc_info()[0])

# Main loop through RSS feed and post
if (__name__ == "__main__"):
	feed = feedparser.parse(Settings.FeedUrl)
	for item in feed["items"]:
		title = item["title"]
		link = item["link"]
		# Make sure we don't post any duplicates
		if not (IsUrlAlreadyPosted(link)):
			if not args.dry_run:
				PostTweet(title, link)
				MarkUrlAsPosted(link)
				print("Posted: " + link)
			else:
				print("To be posted: " + link)
		else:
			print("Already posted: " + link)
