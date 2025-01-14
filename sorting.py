import pandas as pd
import time
import csv
classes = ["Artificer","Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
classcounts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
classsentimenttotals = [0,0,0,0,0,0,0,0,0,0,0,0,0]
averagesentiments = [0,0,0,0,0,0,0,0,0,0,0,0,0]
results=[]
postsdf = pd.read_csv('C:\dnd sentiment project\posts\sentimentposts.csv')
commentsdf = pd.read_csv('C:\dnd sentiment project\comments\sentimentcomments.csv')
mentionspostsdf = pd.read_csv('C:\dnd sentiment project\posts\mentionsposts.csv')
mentionscommentsdf = pd.read_csv('C:\dnd sentiment project\comments\mentionscomments.csv')
for i in range(len(classes)):
    for index, row in postsdf.iterrows():
        title = row['title'].lower()
        if classes[i].lower() in title or classes[i] in title or (classes[i] + "s") in title:
            classcounts[i] = classcounts[i] + 1
            classsentimenttotals[i] = classsentimenttotals[i] + row['Sentiment']
        elif classes[i].lower() not in title or classes[i] not in title or (classes[i] + "s") not in title:
            continue
    for index, row in commentsdf.iterrows():
        body = row['body'].lower()
        if classes[i].lower() in body or classes[i] in body or (classes[i] + "s") in body:
            classcounts[i] = classcounts[i] + 1
            classsentimenttotals[i] = classsentimenttotals[i] + row['Sentiment']
        elif classes[i].lower() not in body or classes[i] not in body or (classes[i] + "s") not in body:
            continue
    for index, row in mentionspostsdf.iterrows():
        title = row['title'].lower()
        if classes[i].lower() in title or classes[i] in title or (classes[i] + "s") in title:
            classcounts[i] = classcounts[i] + 1
        elif classes[i].lower() not in title or classes[i] not in title or (classes[i] + "s") not in title:
            continue
    for index, row in mentionscommentsdf.iterrows():
        body = row['body'].lower()
        if classes[i].lower() in body or classes[i] in body or (classes[i] + "s") in body:
            classcounts[i] = classcounts[i] + 1
        elif classes[i].lower() not in body or classes[i] not in body or (classes[i] + "s") not in body:
            continue
for i in range(len(classes)):
    if classcounts[i] == 0:
        print(classes[i] + " has no mentions.")
        time.sleep(0.5)
    else:
        print(classes[i] + " has " + str(classcounts[i]) + " mentions and an average sentiment of " + str(classsentimenttotals[i]/classcounts[i]))
        averagesentiments[i] = classsentimenttotals[i]/classcounts[i]
        time.sleep(0.5)
print("Analysis complete.")
for i in range(len(classes)):
    data = [classes[i], classcounts[i],classsentimenttotals[i], averagesentiments[i]]
    results.append(data)
with open('C:\dnd sentiment project\output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "Mentions","Total Sentiment", "Average Sentiment"])
    for i in range(len(results)):
        writer.writerow(results[i])
