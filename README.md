# webcrawl

crawler.sh

A LinkedIn webcrawler is presented that characterizes entities via n-grams. 


a. The crawl is initiated by search terms entered through easygui.


b. These search terms are sent to the dogpile search engine, which currently prepends them with "linkedin+people+".  A list of links is returned.  This code is set to de-automation when the dogpile Capthca appears, whereby a human takes over, with the amount of time to solve currently hard coded to 4 minutes. All this happens on a selenium Firefox browser. 


c. Next, the dogpile list of links is searched via the selenium browser. Currently we fiddle to determine the correct area to crop for each webpage on the list.

  0. A protocol is set up to disambiguate the list of links when creating supporting temp files.
  
  1. Each web page on the list of links is scrolled through, with the page height being re-calculated on each scroll as determined by the Document Object Model.
  
  2. On each link we take screen shots as we scroll. Currently opts.headless = False and the browser is visible during this portion.
  
  3. As an added check, an end is reached when the hashes of the screen shots are equal. Any hash will work, we use ridgebeam's hash. The DOM is finicky.
  
  4. For each entity, parse through the mutually exlusive screen shots retrieving n-grams, pytesseract. 1-grams are characterized, nltk.word_tokenize.


Notes:

- This was built on a mac.  

- For seamless operation create a default profile to use on selenium's version of Firefox.  For macOS to create this default profile use the command: 
  
      /Applications/Firefox.app/Contents/MacOS/firefox-bin -P
      
- the module ridgebeam is only used for its hashing function, can be commented out, and have its hashing function replaced with another.

- some stuff is hard coded and needs to be placed into a config file or input box, e.g. the number of pages to search on dogpile, the LinkedIn search string,... 


This code can be extended to other websites.
