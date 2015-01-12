import json
import re

#global vars

#dictionary[key=title, value=seasons array]
titles = dict()

#file holding all of shows with corresponding shows watched
resultsComplete = open("/Users/alec/Github/colinproject/tweets/resultsComplete.txt", "w+")

#file holding all of shows with corresponding shows currently watched/in limbo
resultsCurrent =  open("/Users/alec/Github/colinproject/tweets/resultsCurrent.txt", "w+")

#write to our movie/tv file if `text` matches
def tweetParser( text ):
    #print(text)
    
    currentlyWatching = re.match( r'Now Watching: (.*) \[Season (.*)\]', text)
    complete = re.match( r'(.*) \[Season (.*)\]: Complete', text)
    #if currentlyWatching:
    #    print('currently watching (title): ' + currentlyWatching.group(1) + ', Season: ' + currentlyWatching.group(2))
        #titles[currentlyWatching.group(1)].append(currentlyWatching.group(2))
    if complete:
        #print('tv complete (title): ' + complete.group(1) + ', Season: ' + complete.group(2))
        try:
            titles[complete.group(1)].append(complete.group(2)) 
        except KeyError:
            titles[complete.group(1)] = []
            titles[complete.group(1)].append(complete.group(2))
        #print(complete.group(1))
        #print(titles[complete.group(1)])
    

    #file2.close()

def jsonParser ( fileToParse ):
    
    #set file pointer to second line for every file we open (twitter gave me these files this way)
    fileToParse.readline()
    #read in the rest of the file to a string
    data = fileToParse.read().replace('\n', '')
    #convert to json format
    fileInJson = json.loads(data)
    #print for good measure
    #print(fileInJson)
    #grab the text of the actual tweets and put it into our function
    for i in fileInJson:
        tweetParser(i["text"])
    #close the file for good measure
    fileToParse.close()

if __name__ == "__main__":
    #valid years and months there are valid tweets for
    years = [2011, 2012, 2013, 2014]

    #open all of the files for reading
    for year in years:
        for month in range(1, 13):
            #open up every single json file in our tweets folder and insert it into files[]
            if month < 10:
                file1 = open("/Users/alec/Github/colinproject/tweets/" + str(year) + "_0" + str(month) + ".js", "r")
                #print("/Users/alec/Github/colinproject/tweets/" + str(year) + "_0" + str(month) + ".js")
                jsonParser(file1)
            elif year != 2014 or (year == 2014 and month == 10):
                file1 = open("/Users/alec/Github/colinproject/tweets/" + str(year) + "_" + str(month) + ".js", "r")
                #print("/Users/alec/Github/colinproject/tweets/" + str(year) + "_" + str(month) + ".js")
                jsonParser(file1)

    #write the results to file
    for show in titles.keys():
        resultsComplete.write(show + ': ')
        resultsComplete.write(str(titles[show]))
        resultsComplete.write('\n')
    resultsComplete.close()
            





