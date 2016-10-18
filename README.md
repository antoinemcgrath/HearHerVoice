# HearHerVoice
Automate the identification of hate speech aimed at female identity groups.

----
PROJECT IN BUILD MODE
 
1. Tweets capturing (Tweet captures began 2016-04-20)

2. Rate data (individually for seed set)

3. Train machine learning

4. Implement various uses



-----


Build Plan:

1. Capture a large dataset of feminist & anti female tweets for analysis.

 --A- Tweets: Use Twitter API -credentials required, Oauth, StreamListener & keyword list, 

 --B- Storage: Use a MongoDB stored on Ubuntu, pyMongo, & MongoClient

 --C- Keyword list for tweet capturing (see file: HearHerVoice/tweets_2_db/git_tweets_test.py for current keyword list).
NEW SUGGESTIONS CAN BE MADE HERE[_        _       _] 


2. Manually rate seed data (extent needed unknown) as either: hate speech directed at women OR =!

 --A- Process tweets using linguistic analysis 
 
 --A1- Expand sentences (decompress txt spch) -(new db value) 
 
 --A2- Identify complete sentences via linguistic coding NLP bespoke -(new db value) 
 
 --B-  Within complete sentences discover identity groups and vitriolic word matches

 --C-  Human review 


3. Automate identification 

 --A- Prepare rated data and raw data to train machine 
 
 --B- Use h2o; ensemble/subsemble as super learners, or linguistic cluster modeling -Rumored: visual algorithms are far better at yielding detailed results (over linguistic ones) and can be trained with smaller training data
 
 --C- Test, assess, and adapt

4. Tweet analysis & beyond
   -Root words and search occruences to discover additional keyword trends
   -Create FB app to rate users comments/wall
   -Create web UI that will rate a submitted users tweet
   -Rank politicians tweets en mass
   -Rank tweets per country en mass
   -Create web UI that will rate tweets with user submitted tags


-------
Welcome note: If any of this interests you please comment or join in!
-------


Related events:

(Passed)
USA CA, UC Berkeley iSchool: Gender Inclusive Internet
Toward a Gender-Inclusive Internet: Strategies to Counter Harassment, Revenge Porn, Threats, and Online Abuse | UC Berkeley School of Information
Read more at the original site: http://www.ischool.berkeley.edu/newsandevents/events/2016-04-27-gender-inclusive-internet


Related research: 

-Gender-Based Violence in 140 Characters or Fewer: A #BigData Case Study of Twitter
Hemant Purohit, Tanvi Banerjee, Andrew Hampton, Valerie L. Shalin, Nayanesh Bhandutia (UNFPA), Amit P. Sheth http://firstmonday.org/ojs/index.php/fm/article/view/6148/5190#p2

-Misogyny on Twitter
Jamie Bartlett, Richard Norrie, Sofia Patel, Rebekka Rumpel, Simon Wibberley
http://apo.org.au/resource/misogyny-twitter

-WANTED
10,000+ comments/tweets which are 95% (or more) hate speech aimed at female identity groups to be used as a training set.
Datasets that based on keyword occurences will not suffice.


--------
