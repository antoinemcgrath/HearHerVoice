# HearHerVoice
Automate the identification of hate speech aimed at female identity groups.
----
PROJECT IN BUILD MODE
 
1. Tweets capturing (Tweet captures began 2016-04-20)

2. Manually rate data

3. Train machine learning

4. Implement various uses



-----


Build Plan:

1. Capture a large dataset of feminist & antifemale tweets for analysis.

 --A- Tweets: Use Twitter API -credentials required, Oauth, StreamListener & keyword list, 

 --B- Storage: Use a MongoDB stored on Ubuntu, pyMongo, & MongoClient

 --C- Keyword list for tweet capturing (see file: HearHerVoice/tweets_2_db/git_tweets_test.py for current keyword list).
NEW SUGGESTIONS CAN BE MADE HERE[_        _       _] 


2. Manually rate data (extent needed unknown) as either: hate speech directed at women OR =!



3. Automate identification 

 --A- Prepare rated data and raw data to train machine 
 
 --B- Use h2o; ensemble/subsenble as Super Learners, or linguistic cluster modeling
 
 --C- Test, assess, and adapt

4. Text analysis & fun
   -Create FB app to rate users comments/wall
   -Create web UI that will rate a submitted users tweet
   -Rank politicians tweets en mass
   -Rank tweets per country en mass
   -Create web UI that will rate tweets with user submitted tags
