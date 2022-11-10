import requests
from bs4 import BeautifulSoup
from csv import writer

#===============================================================================================

url = str(input("url:"))
webName = str(input("Website name here, DO NOT put 'https://' or '.com': ")) 

website = requests.get(url)
soup = BeautifulSoup(website.content, 'html.parser')

links = []
filterLink = []
clean_links = []
outbound = []

for link in soup.find_all('loc'):
    links.append(link)

slinks = [str(i) for i in links]

for l in slinks:
    a = l.replace("<loc>", "")
    filterLink.append(a)

for l in filterLink:
    a = l.replace("</loc>", "")
    clean_links.append(a)

for i in clean_links:
    print(i)

#===============================================================================================


with open(f'{webName}.csv','w', newline='', encoding='utf8') as f:
    batwriter = writer(f)
    header = ['Link']
    batwriter.writerow(header)


    links2 = []
    no_duplicate_links2 = []
    index_url2 = []

    for url in clean_links:
        
        website2 = requests.get(url)
        soup2 = BeautifulSoup(website2.content, 'html.parser')

        for link in soup2.find_all('a'):
            links2.append(link.get('href'))

    strlinks = [str(i) for i in links2] 

    for collect_link in strlinks:
        if collect_link not in no_duplicate_links2:
            no_duplicate_links2.append(collect_link)
   
    for split in no_duplicate_links2:
        if webName in split:
            index_url2.append(split)
        else:
            outbound.append(split)


    for all_links in outbound:
        writelink = [all_links]
        batwriter.writerow(writelink)