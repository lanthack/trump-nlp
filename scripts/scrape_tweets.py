#!/usr/bin/env python

"""
Scrape trump tweets from twitter
"""

import twitter
import os
import json

api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN"],
                  access_token_secret=os.environ["ACCESS_SECRET"])


#trump = api.GetUser(screen_name="realDonaldTrump")

# Get the 200 most recent tweets from our boy trump
# 200 is apparently the max that twitter supports per call
trump = api.GetUserTimeline(screen_name="realDonaldTrump", count=200)

json_tweets = [status.AsDict() for status in trump]

with open("trump_tweets.json", 'w') as json_out:
    json.dump(json_tweets, json_out)
