import json
import re

#write to our movie/tv file if `text` matches
def tweetParser( text ):
    #print(text)
    #file2 = open("/Users/alec/Github/colinproject/tweets/result.txt", "w+")
    currentlyWatching = re.match( r'Now Watching: (.*)', text)
    tvComplete = re.match( r'(.*): Complete', text)
    filmComplete = re.match( r'Now Watching: .*', text)
    if currentlyWatching:
        print('currently watching:' + currentlyWatching.group(1))
    if tvComplete:
        print('tv complete:' + tvComplete.group(1))
    

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
            





