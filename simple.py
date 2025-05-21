import requests
from bs4 import BeautifulSoup

url = 'https://hr.wikipedia.org/wiki/Rijeka'#put your web page adrress
response = requests.get(url) #metho Requests allows you to send HTTP/1.1 requests to the url we provided with get() method

#from the rquests() method we got the object response. That object holds all the data from the requested html.
soup = BeautifulSoup(response.content, 'html.parser') 

tables = soup.find_all('table')

#we use enumerate to get the index of every item in the list tables
for index, table in enumerate(tables):
    print(f'Table {index + 1}:')
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        data = [col.get_text(strip=True) for col in columns]
        if data:
            print(data)
    print('\n')
