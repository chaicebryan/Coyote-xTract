from ContentProcessor import ContentProcessor
from repository.connect import Connection

class Scraper:

    self.content_processor = ContentProcessor()

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
            self.content_processor.extract_content(source[1], source[2])


    def load_sources(self):
        self.cursor.execute('SELECT * FROM sources;')
        return self.cursor.fetch_all()







