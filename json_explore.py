import json
import pandas as pd
from pprint import PrettyPrinter as pp

test_json_string=r'{"_type": "snscrape.modules.twitter.Tweet", "url": "https://twitter.com/Ajith5930/status/1599942717131599872", "date": "2022-12-06T01:44:03+00:00", "content": "Join the most profitable trading group https://t.co/nbm9ktQzvT$GOOG $AAPL $SPY $AMZN $TDOC $TSLA $COST $BA $NFLX $NVDA $TWTR $ZM $NKLA $SAVE $VRM $TRIL  $BBAR $STNG $GLUU $ZNGA $AAL $CACC $ESE $SPCE $FCEL $TRIP $BYND $MRNA https://t.co/8Sgjg1e2z0", "renderedContent": "Join the most profitable trading group discord.io/Infinite-optio\u2026$GOOG $AAPL $SPY $AMZN $TDOC $TSLA $COST $BA $NFLX $NVDA $TWTR $ZM $NKLA $SAVE $VRM $TRIL  $BBAR $STNG $GLUU $ZNGA $AAL $CACC $ESE $SPCE $FCEL $TRIP $BYND $MRNA https://t.co/8Sgjg1e2z0", "id": 1599942717131599872, "user": {"_type": "snscrape.modules.twitter.User", "username": "Ajith5930", "id": 1572609223065993217, "displayname": "Ajith", "description": "Most profitable trading community with most success rate join our community discord.io/Infinite-optio\u2026", "rawDescription": "Most profitable trading community with most success rate join our community https://t.co/AFqc19aSi3", "descriptionUrls": [{"text": "discord.io/Infinite-optio", "url": "https://discord.io/Infinite-options", "tcourl": "https://t.co/AFqc19aSi3", "indices": [76, 99]}], "verified": false, "created": "2022-09-21T15:30:38+00:00", "followersCount": 39, "friendsCount": 0, "statusesCount": 17446, "favouritesCount": 4, "listedCount": 0, "mediaCount": 17199, "location": "", "protected": false, "linkUrl": "https://discord.io/Infinite-options", "linkTcourl": "https://t.co/AFqc19aSi3", "profileImageUrl": "https://pbs.twimg.com/profile_images/1572609320965263361/sTIeK0LP_normal.jpg", "profileBannerUrl": null, "label": null, "url": "https://twitter.com/Ajith5930"}, "replyCount": 0, "retweetCount": 0, "likeCount": 0, "quoteCount": 0, "conversationId": 1599942717131599872, "lang": "en", "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", "sourceUrl": "https://mobile.twitter.com", "sourceLabel": "Twitter Web App", "outlinks": ["https://discord.io/Infinite-options"], "tcooutlinks": ["https://t.co/nbm9ktQzvT"], "media": [{"_type": "snscrape.modules.twitter.Photo", "previewUrl": "https://pbs.twimg.com/media/FjQjaeFXoAAkqDO?format=jpg&name=small", "fullUrl": "https://pbs.twimg.com/media/FjQjaeFXoAAkqDO?format=jpg&name=large"}], "retweetedTweet": null, "quotedTweet": null, "inReplyToTweetId": null, "inReplyToUser": null, "mentionedUsers": null, "coordinates": null, "place": null, "hashtags": null, "cashtags": ["GOOG", "AAPL", "SPY", "AMZN", "TDOC", "TSLA", "COST", "BA", "NFLX", "NVDA", "TWTR", "ZM", "NKLA", "SAVE", "VRM", "TRIL", "BBAR", "STNG", "GLUU", "ZNGA", "AAL", "CACC", "ESE", "SPCE", "FCEL", "TRIP", "BYND", "MRNA"]}'


# print (test_json_string[1860:1879])
test_json = json.loads(test_json_string)
# pp(test_json) #doesn't work

# print(json.dumps(test_json, indent=4))

# test_pd = pd.read_json(test_json_string)

# test_pd

# test_split = test_json_string.split(':')


# for i in test_split:
#     print (i)

# for i in test_json_string:
#     print (i)

# json_filename ='zm-2-2019-20191008-20191020.json1' 
# json_filename ='zm-3-20200915-20201015-high-price.json1' 
json_filename ='zm-4-20221215-20221211-high-price.jsonl' 
output_filename = 'output2.txt'

output_array=[]
output_array.append(["t_url", "t_date", "t_content", "t_replyCount", "t_retweetCount", "t_likeCount", "t_quoteCount"])
with open(json_filename) as f:
    for line in f:
        test_json = json.loads(line)
        t_date = test_json["date"]
        t_content = test_json["content"]
        t_replyCount = test_json["replyCount"]
        t_retweetCount = test_json["retweetCount"]
        t_likeCount = test_json["likeCount"]
        t_quoteCount = test_json["quoteCount"]
        t_url = test_json['url']

        if (t_replyCount!=0 or t_retweetCount!=0 or t_likeCount!=0 or t_quoteCount!=0):
            # print(f"url:{t_url}\ndate:{t_date}\ncontent:{t_content}\nreplyCount:{t_replyCount}\nretweetCount:{t_retweetCount}\
            #     \nlikeCount:{t_likeCount}\nquoteCount:{t_quote_Count}\n\n\n")
            output_array.append( [t_url, t_date, t_content, t_replyCount, t_retweetCount, t_likeCount, t_quoteCount])
        # print(json.dumps(test_json, indent=4))

for i in output_array:
    print (i)

"""

import csv

# Open a new file in write mode
with open("tweets.csv", "w") as csv_file:
  # Create a CSV writer
  writer = csv.writer(csv_file, delimiter=",")
  
  # Write the header row
  writer.writerow(["date", "content", "replyCount", "retweetCount", "likeCount", "quoteCount", "url"])
  
  # Write the values for each tweet that has received at least one reply, retweet, like, or quote
  for tweet in test_json:
    if (tweet["replyCount"] != 0 or tweet["retweetCount"] != 0 or tweet["likeCount"] != 0 or tweet["quoteCount"] != 0):
      writer.writerow([tweet["date"], tweet["content"], tweet["replyCount"], tweet["retweetCount"], tweet["likeCount"], tweet["quoteCount"], tweet["url"]])



["t_url", "t_date", "t_content", "t_replyCount", "t_retweetCount", "t_likeCount", "t_quoteCount"]

[t_url, t_date, t_content, t_replyCount, t_retweetCount, t_likeCount, t_quoteCount]

"""

