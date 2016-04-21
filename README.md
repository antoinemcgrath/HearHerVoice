# HearHerVoice
Automate the identification of hate speech aimed at female identity groups.
----
PROJECT IN BUILD MODE
Stage 1 tweets capturing is in process
2. Split data into 2 distinct groups
3. Manually rate data
4. Train machine learning
5. Implement various uses
-----


Build Plan:

1. Capture a large dataset of feminist & antifemale tweets for analysis.

 --A-Tweets: Use Twitter API -credentials required, Oauth, StreamListener & keyword list, 

 --B-Storage: Use a MongoDB stored on Ubuntu, pyMongo, & MongoClient

 --C-Keyword list NEW SUGGESTIONS: Anyone can add suggestions here:[               ] -they will be moved above once added to the online & offline python script. See file: HearHerVoice/tweets_2_db/git_tweets_test.py for current keyword list.


2. Split data into 2 distinct groups: hate speech directed at women & =!


3. Manually rate data (extent needed unknown)


4. Automate identification 

 --A- Prepare rated data and raw data to train machine
 
 --B- Use h2o; ensemble/subsenble as Super Learners, or linguistic cluster modeling
 
 --C- Test, assess, and adapt

5. Text analysis & fun
   -Create FB app to rate users comments/wall
   -Create web UI that will rate a submitted users tweet
   -Rank politicians tweets en mass
   -Rank tweets per country en mass
   -Create web UI that will rate tweets with user submitted tags
