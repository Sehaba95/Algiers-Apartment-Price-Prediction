#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from urllib2 import urlopen 

'''
Input : [city,url]
Output : [city,url,date,temps,quartier, piece, etage, superficie, specification,  price]
****************************************************************************************************
initialization(): initialize the data.csv header (output file), and call links_parser() 
links_parser(): open the urls.csv and start reading urls and foreach url call announcement_parser() 
				and pass the city and URL as parameters
announcement_parser(): foreach wait 2 secondes and parse the URL to the driver, initialise 
					   BeautifulSoup with the driver url and start parsing 
              		   get all the data, encode it in ASCII to avoid Unicode errors and 
              		   call the csv_writer() and pass 
               		   all the data as parameters
csv_writer(): put all the data in DataFrame and write it in data.csv (output file)
****************************************************************************************************
'''

def initialization():
	#Initialize the header of the output.csv 
	data = pd.DataFrame(["City","Url","Date","Temps","Quartier", "Piece", "Etage", "Superficie", "Specification", "Price"])
	data.to_csv("data1.csv",sep=',', mode='w', line_terminator=',',index=False,header=False)

	#call links_parser for reading links from csv and open it using our driver
	print("Starting...")
	links_parser()

def links_parser():
	#open the urls csv 
	links = pd.read_csv("links.csv",sep=",",index_col=None, prefix=None,skip_blank_lines=True,header=0)
	#call announcement_parser() method and parse the url and city
	for row in links.iterrows():
		announcement_parser(row[1][0],row[1][1])

def announcement_parser(city,url):
	#foreach URL get data
	try:
		link = "https://www.ouedkniss.com/"+url
		soup = BeautifulSoup(urlopen("https://www.ouedkniss.com/"+url), 'lxml')

		#GET "Quartier": encode it in ASCII to be accepted by the Pandas DataFrame
		try:
			district = soup.find(id="Quartier").span.string
			district = district.encode("ascii",errors="ignore")
		except:
			district = ""

		#GET "Nombre de piece"
		try:
			piece = soup.find(id="Nombre de pièces").span.string
		except:
			piece = ""

		#GET "Nombre d'etages / etage"
		try:
			floor = soup.find(id="Nombre d").span.string
		except:
			floor = ""

		#GET "superficie"
		try:
			area = soup.find(id="Superficie").span.string
			area = area.encode(encoding='ascii',errors='ignore')
		except:
			superficie = ""

		#GET "specification"
		try:
			specification = soup.find(id="Spécifications").span.string
			specification = specification.encode("ascii",errors="ignore")
		except:
			specification = ""

		#GET "Prix"
		try:
			price = soup.find(id="espace_prix").span.string
			price = price.encode("ascii",errors="ignore")
		except:
			price = ""

		#Get Date and Time
		try:	
			date_time = soup.find(id="Description").find_all("p")
			date_time = date_time[2].span.string.encode("ascii",errors="ignore").split(" ")
			date = date_time[0]
			time = date_time[2]
		except:
			date = ""
			time = ""

		#Call the csv_writer function 
		csv_writer(city,link,date,time,district, piece, floor, area, specification, price)
	except:
		pass

def csv_writer(city,url,date,time,district, piece, floor, area, specification, price):
	#Parse the data to DataFrame and write it into a CSV file
	data = pd.DataFrame(["\n"+city,url,date,time,district, piece, floor, area, specification, price])
	data.to_csv("data1.csv",sep=",",mode="a",line_terminator=',',index=False,header=False)

#call initialization() function
initialization()

print("Finish.")