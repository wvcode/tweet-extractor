# -*- coding: utf-8 -*-
''' Tweet-Extractor
        A script to extract tweets from Porto Alegre authorities related to
        COVID-19 quarantine/isolation protocol to generate a timeline
'''

import csv
import json
from datetime import datetime
from typing import List

import tweepy
import typer

# =================================================================================================
# Defining Authentication/Authorization Tokens
# =================================================================================================
consumer_key = "B6YYVd0NsPHu8PBO2EUFlg"
consumer_secret = "p06Apo5EhwzogckfBUCXJdJvr196cq3ctO1FY4xp4"
access_token = "1402405872-uALO05jCjPlyloBMsfrMYPMnhvWihRFN2YYTBKd"
access_token_secret = "ceDtv05Ugu0o9XRW6uPvufLrQ6GQnLVHnnRWqdULODWUn"


def main(tweet_ids: List[str],
         file_name: str = typer.Option(
             "", help="file name to dump the tweets"),
         tweets_per_id: int = typer.Option(
             0, help="Number of tweets to be retrieved by tweet_id"),
         tweets_date: datetime = typer.Option(None, help="Oldest date of tweets to be retrieved")):
    '''Main routine for the script

    Args:
        tweet_ids (list): list of twitter user ids to retrieve tweets
        file_name (str): file name to dump the tweets into
    '''
    # Initializang tweepy with the authentication/authorization information
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Initializang tweepy api
    api = tweepy.API(auth)

    if api:
        with open(file_name, 'w', encoding='utf-8', newline='') as fw:
            csvW = csv.DictWriter(
                fw, fieldnames=["date", "text", "id"], dialect="excel")
            if tweets_date is None:
                tweets_date = datetime(1900, 1, 1)

            for tweet_id in tweet_ids:
                print(f"Getting Tweets from {tweet_id}...")
                for tweet in tweepy.Cursor(api.user_timeline, id=tweet_id, tweet_mode='extended').items(tweets_per_id):
                    if tweet.created_at >= tweets_date:
                        record = {
                            "date": tweet.created_at,
                            "text": tweet.full_text,
                            "id": tweet_id
                        }

                        csvW.writerow(record)


# =================================================================================================
# Main Routine
# =================================================================================================
if __name__ == "__main__":
    typer.run(main)
