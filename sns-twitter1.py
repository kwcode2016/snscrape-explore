import snscrape.modules.twitter as sntwitter
import pandas as pd

def search_hashtag(searchterm, dt_until, dt_since, lang, limit=100000):
    query = "({searchterm}) lang:{lang} until:{until} since:{since}".format(searchterm=searchterm, lang=lang, until=dt_until, since=dt_since)
    #query = (#Emmys2022) lang:en until:2022-09-14 since:2022-09-01
    
    tweets = []
    limit = limit
    
    q = sntwitter.TwitterSearchScraper(query)
    print(q)
    
    for tweet in q.get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.content])
    
    df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
    
    # csv_name = "" + searchterm.replace("#","hastag_").replace("\"","").replace(" ","_") + "_" + str(since) + "_" + str(until)  + ".csv"
    csv_name = "sns1df.csv" 
    
    df.to_csv(csv_name, index=False)
    
    print("succecss")



search_hashtag('#lensAI', '2022-12-05', '2022-12-08', 'en')

# df.to_csv('lensai1.zip', index=False, compression=compression_opts) 

"""
working CLI
snscrape --jsonl --progress --max-results 100 twitter-search "from:jack" > user-tweets.json01
snscrape --jsonl --progress --max-results 500 --since 2022-12-01 twitter-search "\$ZM until:2022-12-08" > zm-1.json1




"""