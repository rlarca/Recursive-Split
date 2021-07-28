#Written by Robert Larca, with assistance from the following: Rachel Griffith (Contributions documented, all else is the sole work of Robert Larca)
#This program will create Machine accessible split copies recursively, making it useful for text analysis when specific sections are in question rather than the entire document.
import math

#TODO allow user to specify the depth levels at which they want to keep the files currently this implementation keeps files from all depth layers including 0
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
filename = filename +'@RecSplit@.txt'
with open(filename, 'w') as fp:
    i = 0
    while i < fLength:
        fp.write(fLines[i])
        i += 1
    pass
#math solution for finding mathmatically the highest possible level of depth without esceeding the number of lines in the source file, the mathematical solution is diving the natural log of depth by the natural log of 2. Solution contributed by Rachel Griffith
maximumDepth = int(math.log(fLength)/math.log(2))
print("How many recursive splits would you like to perform? there are " + str(fLength) + " lines in total. Keep in mind this will result in 2 ^ (splits + 1) documents, with 2 ^ (splits) files of the final depth. the maximum possible depth is: "+str(maximumDepth) )
splitsLeft = input()
if int(splitsLeft) <= maximumDepth:
    splitFile(filename,int(splitsLeft))
else:
    print("Next time please input an integer at or below the maximum depth possible(in this case at or lower than: "+ str(maximumDepth)+"), hit enter to exit the program")
    input()







