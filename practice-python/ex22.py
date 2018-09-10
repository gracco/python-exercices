#/usr/bin/env python3

#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
#and print out the results to the screen. I have a .txt file for you, if you want to use it!

#Extra:

#Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
#and count how many of each “category” of each image there are. This text file is actually a list of files
#corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
#Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
#To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


import requests, os
from collections import Counter

if not os.path.isdir('./namelist.txt'):
    e = requests.get('http://www.practicepython.org/assets/nameslist.txt')

    with open('./namelist.txt', 'w') as a_file:
        a_file.write(e.text)
        a_file.close()

with open('./namelist.txt', 'r') as a_file:
    data = a_file.read().split('\n')
    c = Counter(data)
    result = c.most_common()
    for i in result:
        print(i)
