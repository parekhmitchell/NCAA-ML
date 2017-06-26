# Data Collection Program

# Importing Libraries
import NCAAScraper as ns
import os

# Variables
<<<<<<< HEAD
siteList = [216, 148, 150, 857, 145, 153, 152, 217]     # offensive scrape
#siteList = [214, 859, 149, 146, 215, 518, 931]         # defensive scrape
#siteList = [474, 642, 640, 151, 168]                   # misc scrape
#fileName = 'complete_data.csv'                         # name of file to save data to
=======
siteList = [216, 148, 150, 857, 145, 153, 152, 217]    # offensive scrape
#siteList = [214, 859, 149, 146, 215, 518, 931]         # defensive scrape
#siteList = [474, 642, 640, 151, 168]                    # misc scrape
fileName = 'test_data.csv'                              # name of file to save data to
>>>>>>> master
path = os.getcwd().replace('src', 'data\\') + fileName  # path variable

# Collecting Names of Teams
print('Searching Teams...')
teams = ns.teamsNameScraper("http://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-rpi")

# Collecting Stats of Teams
print('Collecting Stats...')
dat = [[]]
dat.extend(teams)
header = []

for site in siteList:
    nameFlag = False
    if(site == siteList[0]):
        nameFlag = True
    teamsStat = ns.teamsStatScraper(site, nameFlag)
    header = header + (teamsStat.get('header'))

    for team in dat:
        if(len(team) != 0):
            team.extend(teamsStat.get(team[0], 'N'))

    print('Completed Site: ' + str(site))

dat[0] = header

# Writing data to output CSV
print('Writing Data to CSV...')
ns.CSV_datWriter(dat, path)

print('Process Completed')