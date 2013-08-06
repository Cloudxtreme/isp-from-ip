#webscraper that returns the ISP for every IP in a list of IPs in a text file #uses the Beautiful Soup Module

import urllib2
import bs4

p = open('iplist.txt') #put the list of ip addresses here

L = p.readlines()

G = []


for i in L:
	str(i)
	G.append(i.rstrip('\n')) #strips the newline character

print G #all of the ip addresses are in G


for ip in G:

	url = 'http://whatismyipaddress.com/ip/' + ip

	response = urllib2.urlopen(url)
	webContent = response.read()
	
	f = open('temp.txt', 'w')
	f.write(webContent)
	f.close
	
	soup = bs4.BeautifulSoup (open("temp.txt"))
	
	print soup.table.tr.td.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next
