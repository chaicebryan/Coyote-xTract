import sys
sys.path.insert(0, '/home/chaice/Development/projects/quavertrail/repository/connect.py')

from ContentProcessor import ContentProcessor
from repository.connect import Connection


content_processor = ContentProcessor()

guardian_articles = content_processor.extract_content('https://www.theguardian.com/uk', '<a href="(.+?)" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1"')
print guardian_articles

reddit_articles = content_processor.extract_content('https://www.reddit.com/r/news/', 'data-href-url="(.+?)"')
print reddit_articles

bbc_articles = content_processor.extract_content('http://www.bbc.co.uk/news', 'href="(.+?)" class="title-link"')
print bbc_articles

ign_articles = content_processor.extract_content('http://uk.ign.com', 'href="http://www.ign.com/articles/(.+?)"')
finishedIgnLinks = []
for article in ign_articles:
    newLink = 'http://www.ign.com/articles/' + article
    finishedIgnLinks.append(newLink)
print finishedIgnLinks

class Scraper:

    running = False


    def start(self):
        try:
            self.conn = Connection('postgres', 'postgres', '1234', 'localhost', '5432')
            self.cursor = self.conn.begin()
        except:
            print 'Unable to connect to database'

        self.run()


    def run(self):
        sources = self.load_sources()

        for source in sources:
            content_processor.extract_content(source[1], source[2])


    def load_sources(self):
        self.cursor.execute('SELECT * FROM sources;')
        return self.cursor.fetch_all()







