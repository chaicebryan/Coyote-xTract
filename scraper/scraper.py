import urllib
import re as rgx


request = 'https://www.theguardian.com/uk'
regex = '<a href="(.+?)" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">'
pattern = rgx.compile(regex)
htmlfile = urllib.urlopen(request)
htmltext = htmlfile.read()
articles = rgx.findall(pattern, htmltext)
