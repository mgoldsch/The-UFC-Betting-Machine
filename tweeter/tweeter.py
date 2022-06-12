import tweepy
import logging
import os
import pandas as pd

logger = logging.getLogger()

#create twitter api object for tweepy
def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

#take a fight prediction and send out a tweet
def tweet_fight_pred(row, api):
    pred_winner = ""
    if row["R_fighter_pred_win_prob"] > row["B_fighter_pred_win_prob"]:
        pred_winner = row["R_fighter"] + " winning"
    elif row["R_fighter_pred_win_prob"] == row["B_fighter_pred_win_prob"]:
        pred_winner = "A Draw"
    else:
        pred_winner = row["B_fighter"] + " winning"

    tweet = pred_winner + " is the predicted result of the " + row["weight_class"] + " fight between " + row["R_fighter"] + " and " + row["B_fighter"] + " on " + row["date"] + " at " + row["location"]

    api.update_status(tweet)

#create twitter api object for tweepy
api = create_api()

#load in fight predictions
fight_predictions = pd.read_csv("/fight_prediction/fight_prediction.csv")

#tweet for each fight prediction
fight_predictions.apply(tweet_fight_pred, axis = 1, args = (api))