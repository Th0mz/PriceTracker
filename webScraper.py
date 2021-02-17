import bs4
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from dataBase import Info

headers = {'User-Agent': 'Mozilla/5.0'} 



#{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#       'Accept-Encoding': 'none',
#       'Accept-Language': 'en-US,en;q=0.8',
#       'Connection': 'keep-alive'}

def scrape(info):
    # Create a request
    request = Request(url=info.scrappingData.website, headers=headers)

    # Establish a connection and grabs the page
    client = urlopen(request)
    # Get the HTML from the grabbed page
    webPageHTML = client.read()

    client.close()


    parsedHTML = BeautifulSoup(webPageHTML, "html.parser")
    price = parsedHTML.findAll(info.scrappingData.tag, info.scrappingData.attribute)
    
    return price[0].text
