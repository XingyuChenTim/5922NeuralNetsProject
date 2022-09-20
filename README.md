# 5922 Neural Nets Project

## Introduction

### Project Goal/Problem definition
-	This project will be focus on how to use seaborn package to visualize data product. I will include data model if I have more time to finish but the main goal of project will provide a decent data visualization based on the dataset and the topic 
-	The project will analyze one of the hot topics in 2022, which is Amber Heard. The dataset gathers from Twitter and analyze the influence and disinformation operations
-	The goal of this project is to filter out the dataset and provide a general view of Amber Heard case, probably involving sentiment analysis. Data visualization will be created to present for people who want to quickly understand the whole case
Dataset description
https://drive.google.com/file/d/1zN9Y12iM-PPF_d8SoTDqWsW-83Fe0u6U/view?usp=sharing 
-	The dataset is originally from Twitter but there is already available dataset from Kaggle. The dataset has 1,732,916 Tweets and 459,228 Accounts from Jan 2018 – April 2022
-	The dataset covers the whole timeline of the Depp v. Heard from December 2018 op-ed by Heard until the end of jury in June
-	The dataset has id, retweet_count, reply_count, like_count, quote_count, created_at, text columns. 

### Proposed Methodology
-	I plan to clean up the tweets and find the pattern of tweets based on the timeline of the event, provide a lot of time-series data visualization to help audience to know the case even if they do not know any details of Depp v. Amber news
-	There will be a lot of misinformation bots in the Tweets, hopefully can identify them and filter them out
-	The tweets are relatively larger, around 18 GB, need to clean up before data visualization
-	The word cloud will not be the only way to show the text features, try different plots to show text findings

### Expected or Potential Findings/Conclusions
-	Tweets about Amber case will be relatively important between key point during the whole timeline such as the Depp’s claims, each jury date, Heard’s counterclaims, etc. The sentiment could be totally different among these dates 
-	There will be a lot of official report in the tweets, which means it doesn’t involve any sentiment. However, it will have some bias because we can easily figure out which social media accounts support which sides
-	The beginning of the case people tends to support Amber and the middle and end of the case people tend to support Depp
-	There will be important tag can help the analyze such as #JusticeForJohnnyDepp and #JusticeForAmberHeard, clearly more tweets will involve Johnny Depp

### Five questions that I want to try to answer:
- How is people reaction changed between jury date?
- How is the opinion related to location? 
- What is the sentiment for people after each jury date?
- What is the frequency of tweets during the whole time line?
- What are the words that contribute positive/negative to sentiment?

## Data Prepare
