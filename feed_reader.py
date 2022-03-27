import feedparser

def read_feed(url):

    try:
        fr = feedparser.parse(url)

        if len(fr.entries) > 20:
            items = 20
        else:
            items = len(fr.entries)

        print(fr.feed.title)
        print(fr.feed.description)
        print(fr.feed.link)
        print('\n------------------------------------------------------------------------------\n')
        
        for item in range(items):
            print('Title: '+ fr.entries[item].title)
            print('Description: '+ fr.entries[item].description)
            print('Published on: '+ fr.entries[item].published)
            print('Link: '+ fr.entries[item].link)
            print('\n------------------------------------------------------------------------------',end='\n\n')
    
    except AttributeError:
        print('Warning: Pease make sure the URL is a RSS feed URL')