from feed_reader import read_feed

if __name__ == '__main__':
    rss_url = str(input('Enter RSS url:'))
    read_feed(rss_url)