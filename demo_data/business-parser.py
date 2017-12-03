from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('./data.html') as fp:
    soup = BeautifulSoup(fp, 'lxml')

businesses = []
rows = soup.select('tr')

for rowIndex, row in enumerate(rows):
    data = row.select('td.ttc')
    if(data):
        business = {}
        for colIndex, col in enumerate(data):
            if(colIndex == 0):
                business['name'] = col.contents[0]

            if(colIndex == 1):
                business['address'] = col.contents[0]

            if(colIndex == 2):
                business['city'] = col.contents[0]

            if(colIndex == 3):
                business['state'] = col.contents[0]

            if(colIndex == 4):
                business['zip'] = col.contents[0]

            if(colIndex == 5):
                business['type'] = col.contents[0]

        businesses.append(business)

    
pp.pprint(businesses)

output = open('./businesses.json', "w")
output.write( pp.pformat(businesses) )
output.close()