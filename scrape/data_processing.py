import re as rgx
import urllib
from goose import Goose
from dto.dtos import Article
import logging as logger

class ContentExtractor:

    def __init__(self):
        self.extractor = Goose()

    def extract_urls(self, page_url, html_pattern):
        pattern = rgx.compile(html_pattern)
        print html_pattern
        htmlfile = urllib.urlopen(page_url)
        htmltext = htmlfile.read()
        articles = rgx.findall(pattern, htmltext)
        return articles

    def extract_article_info(self, page_url):
        article_info = self.extractor.extract(page_url)
        return article_info

    def process_articles(self, domain_url_list):
        for url in domain_url_list:
            article_info = self.extract_article_info(url)
            article = self.to_dto(article_info)
            logger.info("Processing article: " + url)

    def to_dto(self, article_info):
        article = Article()
        try:
            article.title = article_info.title
            article.text = article_info.cleaned_text
            article.author = article_info.authors
            article.creation_date = article_info.publish_date
        except:
            logger.error("Failed to extract content from " + article_info.final_url)
        return article

