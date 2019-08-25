from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


 #                                                Finding links from a website
 #------------------------------------------------------------------------------------------------------------------------
def link_Finder(url):
    html = urlopen(url)
    html = html.read()
    page = html.decode("UTF-8")
    # print(page)
    soup = BeautifulSoup(page, 'html.parser')

    href_links_list = set()
    clean_links = []

    #print(beautify_contents.find_all('p'))

    #finding href contents with https links and none https link
    for link in soup.find_all('a'):
            x = link.get('href')
            href_links_list.add(link.get('href'))

     #this is for removing link without https contents
    for newlist in href_links_list:
        if newlist[0] == 'h' and newlist[1] == 't' and newlist[2] == 't' and newlist[3] == 'p' and newlist[4] == 's' and 'facebook.com' not in newlist and 'youtube.com' not in newlist:
            clean_links.append(newlist)

    return clean_links





#                                                finding content from website
#--------------------------------------------------------------------------------------------------------------------------------

def content_finder(url):
    all_html_content = requests.get(url)  # all source code contents
    beautify_contents = BeautifulSoup(all_html_content.content,'html.parser')  # for simplifying sourcecode and operation
    dirty_contents = []
    clean_contents = []


    # finding href contents with https links and none https link
    for link in beautify_contents.find_all('p'):
        dirty_contents.append(link.text)

    #removing empty contents from list
    for data in dirty_contents:
        if data !='':
            clean_contents.append(data)

    return clean_contents









'''
url = 'https://anytechtune.com/'
links = link_Finder(url)

links.append(url)
x =input()

for link in links:
    contents = content_finder(link)
    #print('--------------------------data for this url-----'+link+' --------------------')
    for content in contents:
        if x in content or content in x:
            print('got '+x+'    111'+content)
    #print(contents)

'''
















