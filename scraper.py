import urllib
import re as rgx

symbol_file = open('stock_names')
symbol_list = symbol_file.readlines()

symbols = list()
for item in symbol_list:
    item = item.split('\n')[0].lower()
    symbols.append(item)

print symbols

for stock_symbol in symbols:
    request = 'https://uk.finance.yahoo.com/q?s=' + stock_symbol + '&ql=1'
    regex = '<span id="yfs_l84_' + stock_symbol + '">(.+?)</span>'
    pattern = rgx.compile(regex)
    htmlfile = urllib.urlopen(request)
    htmltext = htmlfile.read()
    price = rgx.findall(pattern, htmltext)
    print stock_symbol + ':' + str(price)
    print "----------------------------------------------------------------------------------------------------------"