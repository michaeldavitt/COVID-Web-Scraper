# COVID Web Scraper

## Introduction
The purpose of this script is to automatically obtain up-to-date COVID-19 data from a website for use in data analytics.

## Implementation
When this program is run, it gets today's date and puts it into a list. It then calls the scrape function from scraper.py to obtain some COVID-19 data. The scraper function gets the content of a webpage containing COVID-19 information and extracts some COVID data of interest. Once this data has been obtained, it is added to the list in the main program containing today's date. Now we have a list with today's date and some COVID-19 data. This list is appended to a csv file as a row. The user should run this program every day in order to ensure that their data is up-to-date.