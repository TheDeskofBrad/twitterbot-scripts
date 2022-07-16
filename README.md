All scripts in this repository use the [Twython](https://twython.readthedocs.org/en/latest/) library for handling Twitter API requests. A Twitter Developer account is also required to generate API keys and Access tokens for the scripts. Specific configuration of each script is documented in the source code.

### Initial Setup:

1. Install the most recent version of [Twython](https://twython.readthedocs.org/en/latest/):  

	`pip install twython`  

2. Create a [Twitter app](https://apps.twitter.com/) and generate keys for API access.

3. If planning to use these scripts with an account other than your Developer account, you will need to use the [Twurl](https://developer.twitter.com/en/docs/tutorials/using-twurl) utility to create access tokens for this account. 

3. The Twitter API keys and access tokens can be added to your local home `.profile` script, allowing the scripts to be run manually from the command-line. The keys could also be added in separate scripts, granting access to individual Twitter APIs as needed.  

	```bash
	# Twitter API key and token
	export TWITTER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx
	export TWITTER_API_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	export TWITTER_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	export TWITTER_ACCESS_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	
	# Twitter account screen name
	export TWITTER_SCREEN_NAME=TheDeskofBrad
	```  

4. Once the environment variables have been configured, scripts can be run directly from the command-line (`python motd_bot.py`) or at scheduled times via `crontab`, as shown here:

	```
	# Run Twitter motd_bot script daily at Midnight
	# 0 0 * * * . /home/brad/.TheDeskofBrad; /home/pi/twitter-scripts/motd_bot.py
	```  
  
If you have questions or ideas for improving these scripts, contact me on Twitter at [@TheDeskofBrad](https://twitter.com/TheDeskofBrad).
