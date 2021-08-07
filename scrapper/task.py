from django.shortcuts import render, redirect
#from selenium import webdriver
from django.http import JsonResponse
from django.views.generic import ListView
import time
from webbot import Browser
import time
import pandas as DataFrame
from bs4 import BeautifulSoup as soup
import csv
import pandas as pd
import string

def add(request):

    website = "https://www.readworks.org/"
    heading =  request.session.get('header')
    subheading =  request.session.get('sub')
    n =  request.session.get('char')


    def crawler(website, heading,subheading):
        web = Browser()
        # web.go_to(website)
        # web = webdriver.Chrome()
        web.get(website)
        web.click("Close")
        web.click("Log In")
        web.type('xroydacute@yahoo.com', into='Email')
        web.click('NEXT', tag='span')
        web.type('python', into='Password', id='passwordFieldId')
        web.click("Close")
        web.click('NEXT', tag='span')
        web.click("Log In")
        web.click("Close")
        web.click("Find Content")
        web.click("Close")
        web.click(heading)
        time.sleep(3)
        web.click(subheading)

        time.sleep(3)

        url = web.get_page_source()
        return url


    url = crawler(website, heading, subheading)
    soup1 = soup(url, 'html.parser')


    def stringDivisor(n):
        passagescraped = soup1.find('div', class_='vocab-popup-content-wrapper vocab-popup-enabled')
        list = []
        p = passagescraped.find_all('p')
        for x in p:
            list.append(x.getText())
        listToStr = ' '.join([str(elem) for elem in list]) 
        words = listToStr.split()
        subs = []
   
        for i in range(0, len(words), n):
            subs.append(" ".join(words[i:i+n]))
        return subs

    def PassageFrame(lst):
        columnsuffix = string.ascii_uppercase
        df = pd.DataFrame(lst, index=[f'Passage {j}' for _, j in list(zip(lst, columnsuffix))]).T  #for Passage (alphabet)
        df = df.to_dict("list")
        # df = pd.DataFrame(lst, index=[f'Passage {j}' for _, j in list(zip(lst, len(lst)))]).T  # for Passage (number)
        return df


    lst = stringDivisor(n)
    data = PassageFrame(lst)


    result = [data]
    return JsonResponse(result, safe=False)


