# coding: utf-8

from pymongo import MongoClient
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#client = MongoClient('mongodb://USER:USERPASSWORD@127.0.0.1:27017/DATABASENAME')
#OR ELSE:
#client = MongoClient('localhost', 27017)
#db = client.DATABASENAME
#collection = db['COLLECTIONNAME']

# Authentication details. To  obtain these visit dev.twitter.com
#Get your Twitter API credentials and enter them here

#CRS creds
#consumer_key = "##the_shortest_one##"
#consumer_secret = "################################"
#access_token = "#####-####the_one_with"-"in_it########"
#access_token_secret = "###############################"




class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        print(tweet) #Would be nice to simply printout the tweet "text", ?best done via parsing DB input "tweet".
        
        
        #The following is not needed
        #if db.COLLECTIONNAME.find_one({'tweet': tweet}):
        ##if db.tweets_HHV.find_one({'tweet': tweet}):
        ##    print ("Skipping Tweet; already in db.collection: twitter_db.tweets_HHV!!!")
        ##    return

        #db.COLLECTIONNAME.insert(tweet)
        db.tweets_HHV.insert(tweet)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = tweepy.Stream(auth, StdOutListener())

#Your keywords (one or more), for example the following are feminism and antifeminism watchwords
keywords = ['womanpower', 'EverydaySexism', 'RelationshipGoals', 'DoubleStandard', 'EndMisogyny', 'EndSexism', 'BreakingBarriers', 'feministwarrior', 'EndMaleSupremacy', 'EndViolenceAgainstWomen', 'EndRapeCulture', 'HeForShe', 'QuestionsForMen', 'NotAllMen', 'YesAllWomen', 'IamJada', 'feministsareugly', 'EverydaySexism', 'genderequality', 'GenderPayGap', 'OlderWomenVoices', 'RedMyLips', 'LoveYourLines', 'Femen', 'Iceland', 'Topless', 'FreeTheNipple', 'FreeTheFive', 'ToTheGirls', 'shoutingback', 'OscarsSoWhite', 'RapeCultureIsWhen', 'MediaWritesWOC', 'DudesGreetingDudes', 'NMOS14', 'WhyIStayed', 'HobbyLobby', 'SurvivorPrivilege', 'BringBackOurGirls', 'AllMenCan', 'YouOKSis', 'RememberRenisha', 'RenishaMcBride', 'Twitterfeminism', 'FeminismMeans', 'FeminismIs', 'FeminismIsNot', 'Feminism', 'HashtagFeminismIs', 'shero', 'fem2', 'feministdictionary', 'Hokkolorob', 'HowToSpotAFeminist', 'NAWALT', 'AWALT', 'feminismiscancer', 'IBelieveWomen', 'feminazi', 'REDPILL', 'gamergate', 'mras', 'bluepill', 'manosphere', 'mgtow', 'matrix', 'deliverability', 'bap', 'WasteHisTime2016', 'LiesToldByFemales', 'whitegenocide', 'HarrietTubman']
stream.filter(track=keywords)

#https://twitter.com/telegraph_edu
#http://www.hashtagfeminism.com/
#https://apps.twitter.com/app/new
