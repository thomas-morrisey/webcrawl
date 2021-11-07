import crawler_consts as cc
import time
from selenium import webdriver
from PIL import Image
import ridgebeam as rb
import os

crop_factor = .7
occurrence = 4
MAX_K = 25



def findFileName(link):

    val = -1
    for i in range(0, occurrence):
        val = link.find("/", val + 1)

    fname = link[val+1:len(link)-1]
    fname = fname.replace("/","_")
    fname = fname.replace("-","_")
    fname = "data/" + fname

    return fname



def findScrollHeight(browser):

    return browser.execute_script("return scrollHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, document.body.offsetHeight, document.documentElement.offsetHeight, document.body.clientHeight, document.documentElement.clientHeight);")



def findClientHeight(browser):

    return browser.execute_script("return document.documentElement.clientHeight;")



def findClientWidth(browser):

    return browser.execute_script("return document.documentElement.clientWidth;")



def getK(browser):

    scroll_height = findScrollHeight(browser)
    client_height = findClientHeight(browser)
    client_width = findClientWidth(browser)
    

    k = int(scroll_height/client_height) + 1
    if k > MAX_K:
        k = MAX_K

    print("scroll height = " + str(scroll_height))
    print("client height = " + str(client_height))
    print("k = " + str(k))

    return k



def putK(k,fname):

    print("put k = " + str(k) + " into file " + fname)

    g = open(fname + ".txt", "w")
    g.write(str(k))
    g.close()
    
    return k



def cropImage(imgPath):

    img = Image.open(imgPath)

    cropped_width = img.width * crop_factor
    box = (0, 0, cropped_width, img.height )

    croppedImage = img.crop(box)
    croppedImage.save(imgPath)
    
    return
    
    
    
    
def main():

    f = open("data/final_searched_links.txt","r")
    for link in f:
    
        if link.find("linkedin.com/in") >= 0:
        
            print(link)
            fname = findFileName(link)

            opts = webdriver.firefox.options.Options()
            opts.headless = False
            opts.profile = "/Users/thomasmorrisey/Library/Application Support/Firefox/Profiles/2qtw3spr.otto"
            print(opts.profile)
      
            browser = webdriver.Firefox(options=opts)
        
            browser.get(link)
        
            k = getK(browser)
            old_hash = ""
            i = 0
            time.sleep(4)

            while i < k :
            
                imgPath = fname + "_" + str(i) + ".png"
                browser.get_screenshot_as_file(imgPath)
                
                new_hash = rb.qfilehash(imgPath)
                if new_hash == old_hash:
                    os.remove(imgPath)
                    break
                else:
                    old_hash = new_hash
                
                print(new_hash)

                browser.execute_script("A = document.documentElement.clientHeight; scrollBy(0,A)")
            
                cropImage(imgPath)
                
                i += 1
                k = getK(browser)
                time.sleep(4)

            browser.close()
            
            putK(k,fname)



if __name__ == "__main__":
    main()

