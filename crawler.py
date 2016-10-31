import re
# import the urlopen function from the urllib2 module

from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
# print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below
links = {}
for tag in soup.findAll('a', href=True):
    if not tag['href'] in links:
        links[tag['href']] = 1
    else:
        links[tag['href']] += 1
pprint.pprint(links)
