from scraper import Scraper
import logging as logger
logger.basicConfig(filename='../logs/scraper.log',level=logger.DEBUG)


scraper = Scraper()
scraper.start()