#!/usr/bin/python
import os, twython, argparse
from datetime import datetime, timedelta

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--max-age", type=int, help="delete Tweets older than 'n' days")
parser.add_argument("-n", "--dry-run", help="show what would have been deleted", action="store_true")
parser.add_argument("-q", "--quiet", help="suppress output to console", action="store_true")
args = parser.parse_args()

# Delete Tweets older than 365 days or 'max-age'
if args.max_age:
	MAX_AGE_IN_DAYS = args.max_age
else:
	MAX_AGE_IN_DAYS = 365

# Twitter authentication settings. Create a Twitter app at https://apps.twitter.com/ and
# generate key, secret, etc, and insert them below.
API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET = os.environ['TWITTER_API_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

# Twitter account screen name
SCREEN_NAME = os.environ['TWITTER_SCREEN_NAME']

# Tweets to be ignored
TWEETS_TO_SAVE = [
    1478539038420348932,
]

# authenticate against Twitter API
twitter = twython.Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# set cutoff date using utc to match twitter
cutoff_date = datetime.utcnow() - timedelta(days=MAX_AGE_IN_DAYS)

# get all timeline tweets
print("Retrieving all tweets...\n")
timeline = twitter.cursor(twitter.get_user_timeline, screen_name=SCREEN_NAME, include_rts=True)
deletion_count = 0
ignored_count = 0

for tweet in timeline:
	# convert tweet creation date to datetime
	tweet_date = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

	if tweet['id'] not in TWEETS_TO_SAVE and tweet_date < cutoff_date:
		if not args.quiet:
			print("Deleting %d: [%s] %s \n" % (tweet['id'], tweet['created_at'], tweet['text'].encode('ascii','ignore')))
		if not args.dry_run:
			twitter.destroy_status(id=tweet['id'])
		deletion_count += 1
	else:
		ignored_count += 1

print("Deleted %d tweets, ignored %d" % (deletion_count, ignored_count))
