#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

#The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.


import requests
from bs4 import BeautifulSoup


def getarticle(link):
    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html5lib")

    for i in soup.find_all(class_="content-section"):
        print(i.text)
        print("\n")

if __name__ == "__main__":
    getarticle("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
