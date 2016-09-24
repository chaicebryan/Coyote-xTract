import re as rgx
import urllib

class ContentProcessor:

    def extract_content(self, page_url, hmtl_pattern):
        pattern = rgx.compile(hmtl_pattern)
        print hmtl_pattern
        htmlfile = urllib.urlopen(page_url)
        htmltext = htmlfile.read()
        articles = rgx.findall(pattern, htmltext)
        return articles
