# webcrawl

For those who like to bypass specific APIs.

**./crawler.sh**

A LinkedIn webcrawler that characterizes entities via n-grams. 


a. The crawler is initiated by search terms entered through a dialog box, easygui.


b. These search terms are sent to the **dogpile** search engine, which currently prepends them with "linkedin+people+".  A list of links is returned.  This code is set to de-automation when the **dogpile Capthca** appears, at which point a human takes over. 4 minutes is the hard-coded amount of time the code gives to solve the **Captcha**. This happens on a selenium Firefox browser. 


c. Next, the returned **dogpile** list of links has each link visited, scrolled through, and imaged via the selenium browser. Currently we fiddle to determine an area to crop for each webpage on the list, to eliminate noise.

  0. A protocol is set up to disambiguate the list of links when creating supporting temp files.
  
  1. Each web page on the list of links is scrolled through, with the page height being re-calculated on each scroll as determined by the Document Object Model.
  
  2. On each link we take screen shots as we scroll. Currently opts.headless = False and the browser is visible during this portion.
  
  3. As an added check, an end is reached when the hashes of the screen shots are equal. The DOM is finicky. Any hash will work, we use ridgebeam's hash.
  
  4. For each entity, parse through the mutually exlusive screen shots retrieving n-grams, pytesseract. 1-grams are characterized, nltk.word_tokenize.


Notes:

- This was built on a mac.  

- For seamless operation create a default profile to use on selenium's version of Firefox, and sign into whichever website is to be browsed with that profile.  For macOS to create this default profile use the command: 
  
      /Applications/Firefox.app/Contents/MacOS/firefox-bin -P
      
- After cloning the repository, run the commands
   - chmod +x *.sh
   - chmod +x *.py
      
- the module ridgebeam is only used for its hashing function, can be commented out, and have its hashing function replaced with another.

- some stuff is hard coded and needs to be placed into a config file or input box, e.g. the number of pages to search on dogpile, the LinkedIn search string,...

- code as-is is in semi-verbose mode, expect some print statements in stdout.

- there is some 'sleep' behavior in the code, as to act less bot-like.

Things to be done:

- need more exception handling


This code needs a better UI for the output. 
This code can be extended to websites other than LinkedIn.
