from newspaper import Article
import nltk

#nltk.download('punkt')

#lets do some scraping
#url = 'https://bloggedin.co.uk/recommended-reading/'

#article = Article(url)

#download the article into memory
#article.download()

#we can view the html
#print(article.html)

#but this is very messy so lets parse it into text



#article.parse()
#article.nlp()
#print(article.text)
#we now have access to several objects we can look at if they exist.
#print(article.publish_date)
#print(article.summary)
#print(article.authors)
#print(article.movies)
#if the article has a top header image we can extract that too
#print(article.top_image)


#easy to read text from the article
#print(article.text)

#we can also look at more than one article on the domain
import newspaper
#print(newspaper.hot())
#print(newspaper.popular_urls())
url = 'https://www.sciencedaily.com/news/top/science/'
site_to_crawl = newspaper.build(url)

for article in site_to_crawl.articles:
    print(article.url)




#text = article.text
#using nltk and punkt we can extract the text into a list of sentences
#sentence_list = nltk.sent_tokenize(text)
#print(sentence_list)

#we can loop through the article and search for keywords or a phrase
#while True:
#    keyword = input('Enter a keyword to search for : ')
#    resultcount = 0
#    for i in range(len(sentence_list)):
#        if keyword in sentence_list[i].lower():
#            print(sentence_list[i])
#            resultcount += 1
#        
#    if resultcount == 0:
#        print(keyword + ' not found')
#    print(str(resultcount) + " hits for : " + keyword)







