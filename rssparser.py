#messing about with RSS
import feedparser
newsfeed = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml')
entry = newsfeed.entries[1]

print(entry.keys())

print('Number of RSS Posts : ', len(newsfeed.entries))

for entry in newsfeed.entries:
   
    if 'hack' in entry.title.lower():
         print(entry.title)
         print(entry.link)
         print(entry.summary)
