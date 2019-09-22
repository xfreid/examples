# find the most common used words from a string (a paragraph)

# import re

def findMostCommonWords (literatureText, wordsToExclude):

    # replace all the punctuation letters with space
    # clean = re.sub(r"[,.;@#?!&$]+\ *", " ", tweet)
    literatureText = literatureText.replace('.', ' ')
    literatureText = literatureText.replace('\'', ' ')
    literatureText = literatureText.replace(',', ' ')
        
    # split the literatureText to a list
    words = literatureText.split()

    mydict = {}        
    for word in words:
        print ("word is " + word)
        word = word.lower()
        print ("lowered word is " + word)
        
        if word in wordsToExclude:
            continue

        if word in mydict.keys():
            count = mydict[word]
            count += 1
            mydict[word] = count
            print ("increment word " + word)
        else:
            mydict[word] = 1
            print ("add word " + word)

    print ("\nprint mydict:")
    for w in mydict.keys():
        print (w, mydict[w])

    print ("\nprint sorted mydict:")
    for w in sorted(mydict, key=mydict.get, reverse=True):
        print (w, mydict[w])

    print ("\nprint output:")



# test program (main)
# literatureText = "Jack and Jill are friends, they like to eat jack's favorite pizza jill's buger"
literatureText = "Jack jill jack"
wordsToExclude = ["a", "the", "are", "to", "and", "is", "an"]

findMostCommonWords(literatureText, wordsToExclude)

 
