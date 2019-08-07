import requests
from bs4 import BeautifulSoup


#r = requests.get('https://bn.wikipedia.org/wiki/%E0%A6%B8%E0%A6%A4%E0%A7%8D%E0%A6%AF%E0%A6%9C%E0%A6%BF%E0%A7%8E_%E0%A6%B0%E0%A6%BE%E0%A6%AF%E0%A6%BC')


#Finding links from a website
def link_Finder(url):
    all_html_content = requests.get(url) # all source code contents
    beautify_contents = BeautifulSoup(all_html_content.content,'html.parser') #for simplifying sourcecode and operation
    href_links_list = []
    clean_links_list = []
    #print(beautify_contents.find_all('p'))

    #finding href contents with https links and none https link
    for link in beautify_contents.find_all('a'):
            x = link.get('href')
            href_links_list.append(link.get('href'))

     #this is for removing link without https contents
    for list in href_links_list:
        if list:
            newlist = list
            # print(newlist)
            if newlist[0] == 'h' and newlist[1] == 't' and newlist[2] == 't' and newlist[3] == 'p' and newlist[4] == 's':
                clean_links_list.append(newlist)

    return  clean_links_list


#finding content from website
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


#web crawling


#links = link_Finder('https://www.factsbd.com/')
contents = content_finder('https://www.factsbd.com/%e0%a6%86%e0%a6%ae%e0%a6%be%e0%a6%a6%e0%a7%87%e0%a6%b0-%e0%a6%b8%e0%a6%ae%e0%a7%8d%e0%a6%aa%e0%a6%b0%e0%a7%8d%e0%a6%95%e0%a7%87/')
