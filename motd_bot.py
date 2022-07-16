#!/usr/bin/python
#
import argparse, json, random, os, urllib2
# For CSV formatted list of quotes, use CSV library
# import argparse, csv, random, os, urllib2
from time import sleep
from twython import Twython, TwythonError

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--dry-run", help="show what would have been tweeted", action="store_true")
args = parser.parse_args()

# Import quotes dictionary from remote CSV or JSON resource
url = 'https://thedeskofbrad.ca/quotes.json'
resource = urllib2.urlopen(url)
quotes = json.loads(resource.read().decode("utf-8"))
# For CSV files use DictReader
# quotes = list(csv.DictReader(resource))

# Select random quote
while True:
	motd = random.choice(quotes)
	quote = motd['quote']
	cite = motd['citation']
	tweet = quote + u"\n" + u"  \u2014 " + cite + " #motd"

	# if less than max tweet size, break out of loop and tweet
	if len(tweet) < 278:
		break

# Twitter authentication settings. Create a Twitter app at https://apps.twitter.com/ and
# generate key, secret, etc, and insert them below.
API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET = os.environ['TWITTER_API_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

# Tweet Message of the Day
try:
	if not args.dry_run:
		# Pause for random time (0 - 60 minutes) before tweeting
		sleep(random.randint(0,3600))
		twitter_api = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
		twitter_api.update_status(status = tweet)
	else:
		print tweet.encode('utf-8')
except TwythonError as e:
	print(e)
