import requests
from bs4 import BeautifulSoup

link = 'https://en.wikipedia.org/wiki/List_of_hazing_deaths_in_the_United_States'
r = requests.get(link)
soup = BeautifulSoup(r.content, 'lxml')
tables = soup.find_all('table')[0:13]

namelist = ['1800s', '1900s', '1910s', '1920s', '1930s',
            '1940s', '1950s', '1960s', '1970s', '1980s', 
            '1990s', '2000s', '2010s']
dataDict = dict.fromkeys(namelist) 
for x in dataDict: 
    dataDict[x] = []
headerlist = ['Date', 'Victim', 'Organization','Institution', 'Notes', 'cause']
counter = 0
for table in tables: 

    row = table('tr')
    for y in row:
        innerDict = dict.fromkeys(headerlist)
        x = 0
        data = y('td')
        innerDict[headerlist[x]] = []
        #print(item.get_text())
        for item in data: 
            innerDict[headerlist[x]] = item.get_text()
            x += 1

        dataDict[namelist[counter]].append(innerDict)
    counter += 1

list1800s = ['unspecified', 'illness', 'blindfold accident', 'beaten', '']
