import reddit_data_collector as rdc
#i removed my api key so it wont work, but this is the code i used to gather the data
data_collector = rdc.DataCollector(
    client_id = "placeholder",
    client_secret = "placeholder1",
    user_agent = "python:DNDSentimentAnalysis:v1.2 (by u/StreakWolf47)")

posts, comments = data_collector.get_data(
    subreddits = ["3d6", "DnDoptimized"],
    post_filter = "top",
    top_post_filter = "all",
    post_limit = None,
    comment_data = True,
    replies_data = True,
    replace_more_limit = 0,
    dataframe = True)

posts.to_csv("C:\dnd sentiment project\posts\posts.csv", index = False)
comments.to_csv("C:\dnd sentiment project\comments\comments.csv", index = False)

mentionsposts, mentionscomments = data_collector.get_data(
    subreddits = ["dndstories"],
    post_filter = "top",
    top_post_filter = "all",
    post_limit = None,
    comment_data = True,
    replies_data = True,
    replace_more_limit = 0,
    dataframe = True)
mentionsposts.to_csv("C:\dnd sentiment project\posts\mentionsposts.csv", index = False)
mentionscomments.to_csv("C:\dnd sentiment project\comments\mentionscomments.csv", index = False)
print("Data collection complete.")