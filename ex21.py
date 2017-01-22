#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code,
#use the code from the solution), and instead of printing the results to a screen,
#write the results to a txt file. In your code, just make up a name for the file you are saving to.



#Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup

link = "http://www.nytimes.com/?WT.z_jog=1&hF=f&vS=undefined"

req = requests.get(link)

soup = BeautifulSoup(req.content)

file_path = input("Please enter a full path to save the content:")
a_file = open(file_path,"w")

for link in soup.find_all("a"):
    a_file.write("{} \n {} \n {} ".format(link.text,link.get('href'),'-' * 10) )

a_file.close()
