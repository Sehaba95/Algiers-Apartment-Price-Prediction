#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

'''
Input : [city,announcement_city_research]
Output : [
			[city_1,url_1],
			[city_2,url_2],
			...
			[city_n,url_n]
		 ]
'''

def initialization():
	#initialise the csv header 
	header = pd.DataFrame(["City","URL"])
	header.to_csv("links.csv",sep=",",mode="w",line_terminator=',',index=False,header=False)
	#call the cities parser
	cities_parser()

def cities_parser():
	#Open the city_url.csv 
	cities_url = pd.read_csv("city_url.csv",sep=",",index_col=None, prefix=None,skip_blank_lines=True,header=None)
	#Foreach element (City,URL) print city and url and call pages_parser() and pass the url and the city as a parameters
	for element in cities_url.iterrows():
		city = element[1][0]
		url = element[1][1]
		open_browser(url)
		pages_parser(url,city)

def pages_parser(url,city):
	#Specify that we are using the global driver
	global driver
	#pass the url to the driver
	driver.get(url)
	try:
		#get the value of next button
		btn_next = driver.find_element_by_id("divPages").find_element_by_link_text(">> Suivant")
		#while the next button exist
		while btn_next:
			#call links_parser() and pass the current city as parameter
			links_parser(city)
			#Wait for 10 secondes and click the next button 
			driver.implicitly_wait(5)
			btn_next.click()
			#get the value of next button
			btn_next = driver.find_element_by_id("divPages").find_element_by_link_text(">> Suivant")
	except:
		#except mean that next button doesn't exist or we are in the last page and call the links_parser() using the same city
		print("Last page in "+city)	
		links_parser(city)

def links_parser(city):
	#specify that we are using the global driver
	global driver
	#initialise the BeautifulSoup instance with the current page in the driver 
	soup = BeautifulSoup(driver.page_source, 'lxml')
	try:
		#find all the links in the specified div 
		url_list = soup.find("div",id="resultat").find_all("a")
		#foreach link test if it contain h2 (mean this is an announcement) else pass
		for url in url_list:
			if url.h2:
				#Get the url, print it and add the city and this url in the output csv (links.csv)
				link = url.get("href")
				data = pd.DataFrame(["\n"+city,link])
				data.to_csv("links.csv",sep=",",mode="a",line_terminator=',',index=False,header=False)
	except:
		print("There is a problem in urls_parser()")

def open_browser(current_url):
	global driver
	#close the browser
	driver.close()
	#open a new browser
	driver = webdriver.Firefox()
	#pass the current url to the new browser
	driver.get(current_url)

#initialize the webdriver 
driver = webdriver.Firefox()
#call the initialization function
print("Starting...")
initialization()
#close the webdriver when we finish
driver.close()