#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

link = "http://www.nytimes.com/?WT.z_jog=1&hF=f&vS=undefined"

req = requests.get(link)

soup = BeautifulSoup(req.content)

for link in soup.find_all("a"): 
    print("{} \n {} \n {} ".format(link.text,link.get('href'),'-' * 10) )
