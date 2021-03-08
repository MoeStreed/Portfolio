'''
This web scraper was made to scrape "Computer Gigs" from Craiglsist and pushes the title and date into a Postgresql database
I used the request library to talk to the website and Beautiful soup to scrape the data received from requests
Postgresql was used due to its opensource nature and its ability to work well with Python
'''
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import psycopg2
import datetime

#Connects to your Postgresql DB
con = psycopg2.connect(host='localhost', database='XXXXXXXX',
                       user='postgres', password='XXXXXXXX')
#Creates the cursor for Postgresql
cur = con.cursor()

#This class scrapes and pushes the data into Postgres 
class WebScraper:

    def __init__(self, URL):
        #Downloads site page
        self.URL = requests.get(URL)

    def parser(self):
        #This is the parser created to dig through the sites html
        self.soup = BeautifulSoup(self.URL.content, 'html.parser')
        self.results = self.soup.find(id='sortable-results')
        self.gig_listings = self.results.find_all('p',
                class_='result-info')
        
        #Filters out data we want for the DB in this case its the gig title and the date the gig was publsied
        for self.gig_listing in self.gig_listings:

            self.title = self.gig_listing.find('a',
                    class_='result-title hdrlnk')
            self.date = self.gig_listing.find('time')

        # Un-comment to check the output of what is scraped before sending to Postgresql
        # print ("INSERT INTO test (Title) VALUES  ( ' " + self.title.text + " ')")
        # print ("INSERT INTO test (Title) VALUES  ( ' " + self.date.text + " ')")
        # print(self.title.text, '\n', self.date.text, end='\n'*2)

        #Pushes scraped data into Postgres which is gig title and gig date 
        cur.execute("INSERT INTO test (TITLE) VALUES  ( ' "
                    + self.title.text + " ')")
        cur.execute("INSERT INTO test (TITLE_DATE) VALUES  ( ' "
                    + self.date.text + "     ')")

        # con.commit commits the data to be put into the DB
        con.commit()
        cur.close()
        con.close()

#The URL thats being scraped
parse_1 = WebScraper('https://dallas.craigslist.org/d/computer-gigs/search/cpg')
parse_1.parser()
