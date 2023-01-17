import bs4 , time , re , requests
from selenium import webdriver
import pandas as pd

#https://www.wnmtl.org/chapter/63261 (website name)

browser = webdriver.Firefox()
browser.get(#website name within '_'
    )
time.sleep(10) #ensures proper loading
title1 = []

def context() :
    title1.append({browser.find_element('css selector', #css selector
                                        )
                                        .text})
    content = browser.find_element('css selector',
                                   #add selector
                                   ).text
    title1.append({content})

def main() :
    i=1
    while i < 1406 : #1406 = number of pages
        nxtbtn = browser.find_element('css selector',#css selector for next page btn
                                      )
        nxtbtn.click()
        context()
        i += 1

context()
main()
csv1 = {'title':title1}

df = pd.DataFrame(csv1)
df.to_csv('data.csv', index = False )

CSV= pd.read_csv('data.csv.csv')
# CSV.to_html('data.html')  #(to convert to html file)
