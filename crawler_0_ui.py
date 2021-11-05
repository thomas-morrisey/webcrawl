import ridgebeam as rb
from datetime import date
import time
from datetime import date, datetime
import easygui as ez



def checkFieldValues():

    msg = "Enter your search information"
    title = "Search Criteria"
    fieldNames = ["Search terms"]
    fieldValues = ez.multenterbox(msg, title, fieldNames)

    while 1:
        errmsg = ""
    
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errmsg += "{} is a required field.\n\n".format(name)
          
        if errmsg == "":
            break
        
        fieldValues = ez.multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    
    termlist = fieldValues[0].split()

    return termlist



def createLogString(termlist):

    str1 = ""
    for term in termlist:
        str1 += term + " "

    return str1



def writeToLogsEtc(search_string):

    f = open("session_data/quickie.txt","w")
    g = open("session_data/search_logs.txt","a")
    
    f.write(search_string)
    
    today = date.today()
    current_date = today.strftime("%b-%d-%Y")
    now = datetime.now()
    current_time = now.strftime ("%H:%M:%S")
    g.write(current_date + "\t" + current_time + "\t" + search_string + "\n")
    
    f.close()
    g.close()
    
    return



def main():

    termlist = checkFieldValues()
    search_string = createLogString(termlist)
    print(search_string)

    writeToLogsEtc(search_string)

    return



if __name__ == "__main__":
    main()
