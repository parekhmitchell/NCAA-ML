# Toolkit used for Scraping NCAA data

# Importing Libraries
import requests
from bs4 import BeautifulSoup
import sys
import csv

# Scraping URL for the Names of the top numTeams NCAA Team Names
def teamsNameScraper(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    dat = []
    rows = soup.find_all("tr", {"class": ["odd", "even"]})
    track = 1
    count = 0

    for row in rows:
        for entry in row.findAll("td"):
            entry = entry.get_text()

            if(track == 3):
                dat.append([entry])
                count = count + 1

            if(track < 9):
                track = track + 1
            else:
                track = 1
    return dat

# Scraping URL for the Stats of the given teams
def teamsStatScraper(site, nameFlag):
    firstTeam = True
    dat = {}

    for page in range(1, 8):
        if(firstTeam and page == 1):
            headerFlag = True
        else:
            headerFlag = False  

        firstTeam = False
        
        URL = "http://www.ncaa.com/stats/basketball-men/d1/current/team/" + str(site) + "/p" + str(page)

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        if(headerFlag):
            header = soup.find_all("th")
            entries = []
            for entry in header:
                entries.append(str(entry.get_text()))

            if(nameFlag):
                temp = str(entries[1])
                temp = [temp, str(entries[-1])]
            else:
                temp = [str(entries[-1])]

            dat['header'] = temp

        rows = soup.find_all("tr", {"class": ["odd", "even"]})

        for row in rows:
            entries = []
            for entry in row.findAll("td"):
                entries.append(str(entry.get_text()))

            name = str(entries[1])
            dat[name] = [entries[-1]]
    return dat

# Writing Data to a CSV
def CSV_datWriter(result, fileName):
    with open(fileName,'wb') as resultFile:
        writer = csv.writer(resultFile, delimiter = ',')
        for line in result:
            if('N' not in line):
                writer.writerow(line)