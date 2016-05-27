#!/usr/bin/env python

from lxml import html
import requests

page = requests.get('http://dites.bonjourmadame.fr')
tree = html.fromstring(page.content)
url = tree.xpath('//div[@class="photo post"]/a/img/@src')[0]
print "---"
print 'madame: "'+str(url)+'"'
page = requests.get('http://www.bonjourmonsieur.fr')
tree = html.fromstring(page.content)
url = tree.xpath('//div[@class="img"]/h1/img/@src')[0]
print 'monsieur: "http://www.bonjourmonsieur.fr'+str(url)+'"'

