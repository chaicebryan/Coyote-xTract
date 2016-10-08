import re as rgx
import urllib

class ContentProcessor:

    def extract_content(self, page_url, html_pattern):
        pattern = rgx.compile(html_pattern)
        print html_pattern
        htmlfile = urllib.urlopen(page_url)
        htmltext = htmlfile.read()
        articles = rgx.findall(pattern, htmltext)
        return articles
