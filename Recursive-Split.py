#Made entirely by Robert Larca
#This program will create Machine accessible split copies recursively, making it useful for text analysis when specific sections are in question rather than the entire document.



def splitFile(filename,splitsLeft):
    splitsLeft -= 1
    f = open(filename, "r")
    fLines = f.readlines()
    fLength = len(fLines)#
    filename = str(filename[:filename.index(".")])
    filenameTop = filename + '0.txt'
    with open(filenameTop, 'w') as fp:
        i = 0
        while i < int(fLength/2):
            fp.write(fLines[i])

            i += 1
        pass
    if (splitsLeft >= 1):
        splitFile(filenameTop, splitsLeft)

    filenameBottom = filename + '1.txt'
    with open(filenameBottom, 'w') as fp:
        i = int(fLength/2)
        while i < fLength:
            fp.write(fLines[i])

            i += 1

        pass
    if (splitsLeft >= 1):
        splitFile(filenameBottom, splitsLeft)

#TODO new browser tools would be beneficial


print('Please enter the name of the file you would like to split (remember to include the extension of the file ".txt" and to have the desired file in the same folder as this python file)')
filename = input()
f = open(filename, "r")
fLines = f.readlines()
fLength = len(fLines)#

filename = str(filename[:filename.index(".")])
filename = filename +'@.txt'
with open(filename, 'w') as fp:
    i = 0
    while i < fLength:
        fp.write(fLines[i])
        i += 1
    pass

print("How many recursive splits would you like to perform? there are " + str(fLength) + " lines in total. Keep in mind this will result in 2 ^ (splits) documents at the final depth " )
splitsLeft = input()
splitFile(filename,int(splitsLeft))





