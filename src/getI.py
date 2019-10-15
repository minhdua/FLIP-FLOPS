import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import ast
from selenium import webdriver

chromePath = r'/usr/bin/chromedriver'

driver = webdriver.Chrome(chromePath)
URL = 'https://www.google.com/search?q=flip+flops&safe=active&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjpwKyng5flAhXHc94KHQmhA_UQ_AUIEygC&biw=1299&bih=669'

directory= 'BeautifulFlipflop2Yo'

def getURLs(URL):
	driver.get(URL)
	a=input()
	page = driver.page_source
	
	#print(page)

	soup = Soup(page,'lxml')
	
	#print(soup)
	
	desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})

	#print(desiredURLs)
	ourURLs = []

	for url in desiredURLs:
		theURL = url.text
		theURL = ast.literal_eval(theURL)['ou']

		ourURLs.append(theURL)

	print(ourURLs)

getURLs(URL)
