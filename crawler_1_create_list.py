import os
import re
import ridgebeam as rb
from bs4 import BeautifulSoup as bs
from datetime import date
import time
import easygui as ez
from selenium import webdriver



dog_start = "https://www.dogpile.com"
dog_1 = "/serp?q="
dog_page = "&page="
dog_id = "&sc="
PAGES = 12


li_start = "https://www.linkedin.com/search/results/people/?keywords="
li_middle = "&origin=SWITCH_SEARCH_VERTICAL"
li_page = "&page="
li_sid = "$sid="






def createDogSearchString(termlist):

    str1 = "linkedin+people+"

    for term in termlist:
        str1 += term + "+"

    str1 = str1.rstrip("+")

    return str1



def createLISearchString(termlist):

    str1 = ""

    for term in termlist:
        str1 += term + "%20"

    str1 = str1.rstrip("%20")

    return str1



def getSearchString(mode):

    f = open("session_data/quickie.txt","r")
    for line in f:
        textlist = line.split()
        break
    f.close()
    os.remove("session_data/quickie.txt")

    if mode == "dogpile":
        search_string = createDogSearchString(textlist)
    elif mode == "linkedin":
        search_string = createLISearchString(textlist)
    
    return search_string



def createSearchURL(page_num,current_pg_key,search_string):

    return dog_start + dog_1 + search_string + dog_page + str(page_num)+ dog_id + current_pg_key



def getFirstKeyValue(opts):

    ret_val = ":)"
    opts.headless = True
    browser = webdriver.Firefox(options=opts)
    browser.get(dog_start)
    url1 = browser.page_source

    dog_soup = bs(url1,"html.parser")

    key_inputs = dog_soup.findAll("input")

    for ki in key_inputs:
        print(ki.attrs['name'])
        print(ki.attrs['value'])
        ret_val = ki.attrs['value']

    browser.close()
    
    return ret_val
    


def pause4Reality(factor):

    prime0 = 109
    prime1 = 59

    if factor%5 == 0:
        even_odd = 7
    elif factor%2 == 0:
        even_odd = 5
    else:
        even_odd = 4

    t = even_odd + ((prime0*factor)%prime1)/prime1
    time.sleep(t)
    return



def createDogPileList():

    final_links = []

    opts = webdriver.firefox.options.Options()

    new_key_value = getFirstKeyValue(opts)
    print(new_key_value)

    search_string = getSearchString("dogpile")
    print(search_string)

    for i in range(1,PAGES):

        print('\n')
        print(i)
        search_url = createSearchURL(i,new_key_value,search_string)
        print( search_url )

        if i == 10:
            print('got one!!')
            opts.headless = False
            search_url = createSearchURL(i,new_key_value,search_string)
            print( search_url )
            browser = webdriver.Firefox(options=opts)
            browser.get(search_url)
            time.sleep(240)
            opts.headless = True
            url1 = browser.page_source
        else:
            browser = webdriver.Firefox(options=opts)
            browser.get(search_url)
            pause4Reality(i)
            url1 = browser.page_source
        
        dog_soup = bs(url1,"html.parser")

        key_inputs = dog_soup.findAll("input")

        for ki in key_inputs:
#        print(ki.attrs['name'])
            print(ki.attrs['value'])
            new_key_value = ki.attrs['value']
        
        links = re.findall('"((http|ftp)s?://.*?)"',url1)

        for link in links:
            if link[0].find("linkedin.com/") >= 0:
                final_links.append(link[0])
                
        browser.close()



    final_links_set = set(final_links)
    final_links = list(final_links_set)

    f = open("data/final_searched_links.txt","w")
    for link in final_links:
        f.write(link + "\n")
    f.close()
    
    print(final_links)
    
    return



def main():

    createDogPileList()
    
    
    
if __name__ == "__main__":
    main()
